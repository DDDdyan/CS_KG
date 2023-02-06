from datetime import datetime
import os
import random
from werkzeug.utils import secure_filename # 从这个工具里面导入安全工作名来判断安全文件名是否正确
from flask import Blueprint
import pymysql.cursors
from flask import request
import json

import pymysql
from dbutils.pooled_db import PooledDB
# 在项目中链接数据是直接通过pymysql，去做的链接请求关闭，每次操作都要独立重复请求
# 比较浪费资源，在并发不大的小项目虽然无感知，但如果有频繁请求的项目中，就会有性能问题
# 通过使用连接池技术，管理来进行优化，DBUnitls是一套Python的数据库连接池包，对链接对象进行自动链接和释放，提高高频高并发下数据访问性能

app_markdown = Blueprint("app_markdown", __name__)
#
#
# # 封装数据库链接
def connectDB():
    connection = pymysql.connect(host='localhost',  # 数据库IP地址或链接域名
                                 user='root',  # 设置的具有增改查权限的用户
                                 password='wdsr20000129',  # 用户对应的密码
                                 database='TPMDatas',  # 数据表
                                 charset='utf8',  # 字符编码
                                 cursorclass=pymysql.cursors.DictCursor)  # 结果作为字典返回游标
    # 返回新的数据库链接对象
    return connection


# @app_product.route("/api/product/list", methods=['GET'])
# def product_list():
#     # 初始化数据库链接
#     connection = connectDB()
#     # 使用python的with..as控制流语句（相当于简化的try except finally）
#     with connection.cursor() as cursor:
#         # 查询产品信息表-按更新时间新旧排序
#         # 查询产品信息表-按更新时间新旧排序 且 状态为0有效
#         sql = "SELECT * FROM `products` WHERE `status`=0 ORDER BY `id` ASC"  # ASC升序；DESC降序（由于新增status所以做了接口优化）
#         cursor.execute(sql)
#         data = cursor.fetchall()
#
#     # 按返回模版格式进行json结果返回
#     resp_data = {
#         "code": 20000,
#         "data": data
#     }
#     return resp_data


basedir = os.path.abspath(os.path.dirname(__file__))

@app_markdown.route("/api/markdown/upload", methods=["POST"])
def markdown_upload():
    f = request.files.get('file')       # 获取前端传给我的文件
    resp_data = {
        "code": 20000,
        "message": "success",
        "data": {"url":''}
    }
    print(f)
    # 获取安全的文件名 正常文件名
    filename = secure_filename(f.filename)
    print('f',f)
    print('f.filename',f.filename)
    print('filename.rsplit('', 1)',filename.rsplit(".", 1))
    # 生成随机数
    random_num = random.randint(0, 100)
    # f.filename.rsplit('.', 1)[1] 获取文件的后缀
    if len(filename.rsplit(".", 1)) > 1:
        filename = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + str(random_num) + "." + filename.rsplit('.', 1)[1]
    else:
        filename = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + str(random_num) + "." + filename.rsplit('.', 1)[0]
    print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/static/" + filename    # basedir 代表获取当前位置的绝对路径
    f.save(file_path)  # 把图片保存到static 中的file 文件名

    # 可以配置生成对应的外网访问的链接
    my_host = "http://127.0.0.1:3001"
    new_path_file = my_host + "/static/" + filename
    # Avatar = new_path_file
    # sql1 = "update user set password = '%s' ,username='%s' , Avatar = '%s'where phoneNum='%s'" % (password,username,Avatar, userAccount)
    # Result = cursor.execute(sql1)
    # db.commit()
    # if Result > 0:
    #     message = 'success'
    # else:
    #     message = 'error'
    # db.close()
    data = {"url": new_path_file}
    payload = json.dumps(data)
    resp_data['data']['url'] = new_path_file
    return resp_data


# [POST方法]实现新建数据的数据库插入
# 更新接口实现可以直接参考添加操作，只是将数据库insert变成根据id条件update操作，更新的时候也需要进行重复的校验
@app_markdown.route("/api/markdown/save", methods=['POST'])
def markdown_save():
    # 按返回模版格式进行json结果返回
    resp_data = {
        "code": 20000,
        "message": "success",
        "data": []
    }

    # 获取请求传递json
    if request.method == "POST":
        if request.content_type.startswith('application/json'):
            # comment = request.get_json()["content"]
            id = request.json.get('id')
            title = request.json.get('title')
            md = request.json.get('md')
            html = request.json.get('html')
        elif request.content_type.startswith('multipart/form-data'):
            id = request.form.get('id')
            title = request.form.get('title')
            md = request.form.get('md')
            html = request.form.get('html')
        else:
            id = request.values.get('id')
            title = request.values.get('title')
            md = request.values.get('md')
            html = request.values.get('html')

    # 初始化数据库链接
    connection = connectDB()
    with connection:
        # 如果没有重复，定义新的链接，进行更新操作
        with connection.cursor() as cursor:
            # 拼接更新语句,并用参数化%s构造防止基本的SQL注入
            # 条件为id，更新时间用数据库NOW()获取当前时间
            sql = "INSERT INTO `markdown` (`id`,`title`,`md`,`html`) VALUES (%s,%s,%s,%s)"

            cursor.execute(sql, (id, title, md, html))
            # 提交执行保存更新数据
            connection.commit()

        return resp_data


@app_markdown.route("/api/markdown/update", methods=['POST'])
def markdown_update():
    # 按返回模版格式进行json结果返回
    resp_data = {
        "code": 20000,
        "message": "success",
        "data": []
    }

    # 获取请求传递json
    if request.method == "POST":
        if request.content_type.startswith('application/json'):
            # comment = request.get_json()["content"]
            id = request.json.get('id')
            title = request.json.get('title')
            md = request.json.get('md')
            html = request.json.get('html')
        elif request.content_type.startswith('multipart/form-data'):
            id = request.form.get('id')
            title = request.form.get('title')
            md = request.form.get('md')
            html = request.form.get('html')
        else:
            id = request.values.get('id')
            title = request.values.get('title')
            md = request.values.get('md')
            html = request.values.get('html')

    # 初始化数据库链接
    connection = connectDB()
    with connection:
        # 如果没有重复，定义新的链接，进行更新操作
        with connection.cursor() as cursor:
            # 拼接更新语句,并用参数化%s构造防止基本的SQL注入
            # 条件为id，更新时间用数据库NOW()获取当前时间
            sql = "update `markdown` set title = %s ,md=%s,html=%s where id = %s"

            cursor.execute(sql, (title, md, html,id))
            # 提交执行保存更新数据
            connection.commit()
            sql1 = "SELECT * FROM `markdown` ORDER BY `id` ASC"  # ASC升序；DESC降序（由于新增status所以做了接口优化）
            cursor.execute(sql1)
            data = cursor.fetchall()
            resp_data['message'] = '更新成功'
            resp_data['data'] = data

        return resp_data


@app_markdown.route("/api/markdown/getArticle", methods=['GET'])
def markdown_getArticle():
    # 初始化数据库链接
    name = request.args.get('name','')
    connection = connectDB()
    # 使用python的with..as控制流语句（相当于简化的try except finally）
    with connection.cursor() as cursor:
        # 查询产品信息表-按更新时间新旧排序
        # 查询产品信息表-按更新时间新旧排序 且 状态为0有效
        sql = "SELECT * FROM `markdown`  where title like '{}'".format(name)  # ASC升序；DESC降序（由于新增status所以做了接口优化）
        cursor.execute(sql)
        data = cursor.fetchall()

    # 按返回模版格式进行json结果返回
    resp_data = {
        "code": 20000,
        "data": data
    }
    return resp_data