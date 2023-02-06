from flask import Blueprint
import pymysql.cursors
from flask import request
import json

import pymysql
from dbutils.pooled_db import PooledDB
# 在项目中链接数据是直接通过pymysql，去做的链接请求关闭，每次操作都要独立重复请求
# 比较浪费资源，在并发不大的小项目虽然无感知，但如果有频繁请求的项目中，就会有性能问题
# 通过使用连接池技术，管理来进行优化，DBUnitls是一套Python的数据库连接池包，对链接对象进行自动链接和释放，提高高频高并发下数据访问性能

app_clicks = Blueprint("app_clicks", __name__)


# 封装数据库链接
def connectDB():
    connection = pymysql.connect(host='localhost',  # 数据库IP地址或链接域名
                                 user='admin',  # 设置的具有增改查权限的用户
                                 password='123456',  # 用户对应的密码
                                 database='TPMDatas',  # 数据表
                                 charset='utf8mb4',  # 字符编码
                                 cursorclass=pymysql.cursors.DictCursor)  # 结果作为字典返回游标
    # 返回新的数据库链接对象
    return connection


@app_clicks.route("/api/clicks/list", methods=['GET'])
def clicks_list():
    # 初始化数据库链接
    connection = connectDB()
    # 使用python的with..as控制流语句（相当于简化的try except finally）
    with connection.cursor() as cursor:
        # 查询产品信息表-按更新时间新旧排序
        # 查询产品信息表-按更新时间新旧排序 且 状态为0有效
        sql = "SELECT * FROM `clicks` ORDER BY `id` ASC"  # ASC升序；DESC降序（由于新增status所以做了接口优化）
        cursor.execute(sql)
        data = cursor.fetchall()

    # 按返回模版格式进行json结果返回
    resp_data = {
        "code": 20000,
        "data": data
    }
    return resp_data


# [POST方法]实现新建数据的数据库插入
@app_clicks.route("/api/clicks/create", methods=['POST'])
def clicks_create():
    # 初始化数据库链接
    connection = connectDB()
    # 定义默认返回结构体
    resp_data = {
        "code": 20000,
        "message": "success",
        "data": []
    }

    # 获取请求传递json body
    body = request.get_data()
    body = json.loads(body)

    with connection:
        # 先做个查询，判断keyCode是否重复（这里的关键词最初定义为唯一项目编号或者为服务的应用名）
        with connection.cursor() as cursor:
            # 查询需要过滤状态为有效的 且 状态为0有效
            select = "SELECT * FROM `clicks` WHERE `title`=%s"
            cursor.execute(select, (body["desc"],))
            result = cursor.fetchall()

        # 有数据说明存在相同值，封装提示直接返回
        if len(result) > 0:
            resp_data["code"] = 20001  # code 定义20001，那么在前端request.js 进行处理的时候，由于不是20000就会拦截，并按照message内容错误提示
            resp_data["message"] = "唯一编码keyCode已存在"
            return resp_data

        with connection.cursor() as cursor:
            # 拼接插入语句,并用参数化%s构造防止基本的SQL注入
            # 其中id为自增，插入数据默认数据设置的当前时间
            sql = "INSERT INTO `clicks` (`id`,`title`,`desc`) VALUES (%s,%s,%s)"
            cursor.execute(sql, (body["keyCode"], body["title"], body["desc"]))
            # 提交执行保存插入数据
            connection.commit()

        # 按返回模版格式进行json结果返回
        return resp_data


# [POST方法]实现新建数据的数据库插入
# 更新接口实现可以直接参考添加操作，只是将数据库insert变成根据id条件update操作，更新的时候也需要进行重复的校验
@app_clicks.route("/api/clicks/update", methods=['POST'])
def clicks_update():
    # 按返回模版格式进行json结果返回
    resp_data = {
        "code": 20000,
        "message": "success",
        "data": []
    }

    # 获取请求传递json
    body = request.get_data()
    body = json.loads(body)
    # 初始化数据库链接
    connection = connectDB()

    with connection:
        with connection.cursor() as cursor:
            # 查询需要过滤状态为有效的 且 状态为0有效
            select = "SELECT * FROM `clicks` WHERE `title`=%s"
            cursor.execute(select, (body["desc"],))
            result = cursor.fetchall()

            # 有数据并且不等于本身则为重复，封装提示直接返回
            if len(result) > 0 and result[0]["id"] != body["id"]:
                resp_data["code"] = 20001
                resp_data["message"] = "唯一编码keyCode已存在"
                return resp_data

        # 如果没有重复，定义新的链接，进行更新操作
        with connection.cursor() as cursor:
            # 拼接更新语句,并用参数化%s构造防止基本的SQL注入
            # 条件为id，更新时间用数据库NOW()获取当前时间
            sql = "UPDATE `clicks` SET `title`=%s,`desc`=%s,`operator`=%s , `update`= NOW() WHERE id=%s"
            cursor.execute(sql, ( body["title"], body["desc"], body['id']))
            # 提交执行保存更新数据
            connection.commit()

        return resp_data


# [DELETE方法]根据id实际删除项目信息
# 按照标准的RefAPI，通过定义methods = delete方法定义请求接口，参数只需要对应数据的id即可，这里并增加一个请求是否传了id的参数校验，这个接口是真正的数据删除，即所谓的硬删除，这个实现当中额外增加一个参数校验的逻辑
@app_clicks.route("/api/clicks/delete", methods=['DELETE'])
def clicks_delete():
    # 返回的reponse
    resp_data = {
        "code": 20000,
        "message": "success",
        "data": []
    }
    # 方式1：通过params 获取id
    ID = request.args.get('id')
    # 做个参数必填校验
    if ID is None:
        resp_data["code"] = 20002
        resp_data["message"] = "请求id参数为空"
        return resp_data
    # 重新链接数据库
    connection = connectDB()
    with connection.cursor() as cursor:
        sql = "DELETE from `clicks` where id=%s"
        cursor.execute(sql, ID)
        connection.commit()
    return resp_data


# [POST方法]根据id更新状态项目状态，做软删除，仅标记状态不做实际数据删除
@app_clicks.route("/api/clicks/remove", methods=['POST'])
def clicks_remove():
    # 返回的reponse
    resp_data = {
        "code": 20000,
        "message": "success",
        "data": []
    }
    ID = request.args.get('id')
    # 做个参数必填校验
    if ID is None:
        resp_data["code"] = 20002
        resp_data["message"] = "请求id参数为空"
        return resp_data
    # 重新链接数据库
    connection = connectDB()
    with connection.cursor() as cursor:
        # 状态默认正常状态为0，删除状态为1
        # alter table products add status int default 0 not null comment '状态有效0，无效0' after `desc`;
        sql = "UPDATE `clicks` SET  WHERE id=%s"
        cursor.execute(sql, ID)
        connection.commit()

    return resp_data


# 搜索接口
@app_clicks.route("/api/clicks/search", methods=['GET'])
def clicks_search():
    # 获取title和keyCode
    title = request.args.get('title')

    # 基础语句定义
    sql = "SELECT * FROM `clicks`"

    # 如果title不为空，拼接tilite的模糊查询
    if title is not None:
        sql = sql + " AND `title` LIKE '%{}%'".format(title)

    # 排序最后拼接
    sql = sql + " ORDER BY `id` ASC"

    connection = connectDB()
    # 使用python的with..as控制流语句（相当于简化的try except finally）
    with connection.cursor() as cursor:
        # 按照条件进行查询
        print(sql)
        cursor.execute(sql)
        data = cursor.fetchall()

    # 按返回模版格式进行json结果返回
    resp_data = {
        "code": 20000,
        "data": data
    }

    return resp_data


'''
# -*- coding:utf-8 -*-
# 改造成持久化的方式python实现mysql的数据的方式，目前支持度较好的有如：PyMySQL（安装依赖包python3 -m pip install PyMySQL）
from flask import Blueprint
import pymysql.cursors

app_product = Blueprint("app_product", __name__)

# 使用用户名密码创建数据库链接
# PyMySQL使用文档  https://pymysql.readthedocs.io
connection = pymysql.connect(host='localhost',  # 数据库IP地址或链接域名
                             user='root',  # 设置的具有增改查权限的用户
                             password='980722dy',  # 用户对应的密码
                             database='TPMDatas',  # 数据表
                             charset='utf8mb4',  # 字符编码
                             cursorclass=pymysql.cursors.DictCursor)  # 结果作为字典返回游标


@app_product.route("/api/product/list", methods=['GET'])
def product_list():
    # 使用python的with..as控制流语句（相当于简化的try except finally）
    with connection.cursor() as cursor:
        # 查询产品信息表-按更新时间新旧排序
        sql = "SELECT * FROM `Products` ORDER BY `Update` DESC"
        cursor.execute(sql)
        data = cursor.fetchall()

    # 按返回模版格式进行json结果返回
    resp_data = {
        "code": 20000,
        "data": data
    }
    return resp_data
'''

'''
# -*- coding:utf-8 -*-
# 创建一个硬编码的一个产品线模块[ /apis/product.py ] ，来配合实现一个vue页面，产品管理显示

 from flask import Blueprint

 app_product = Blueprint("app_product", __name__)

 @app_product.route("/api/product/list",methods=['GET'])
 def product_list():
    # 硬编码返回list
    data = [
        {"id":1, "keyCode":"project1", "title":"实验一", "desc":"实验1的描述", "operator":"admin","update":"2022-05-06"},
       {"id":2, "keyCode": "project2", "title": "实验二", "desc": "实验2的描述", "operator": "user", "update": "2022-05-06"}
    ]
    # 按返回模版格式进行json结果返回
    resp_data = {
        "code": 20000,
        "data": data
    }
    return resp_data
'''
