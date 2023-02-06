from flask import Blueprint
from flask import request
import json
from dbutils.pooled_db import PooledDB
# 在项目中链接数据是直接通过pymysql，去做的链接请求关闭，每次操作都要独立重复请求
# 比较浪费资源，在并发不大的小项目虽然无感知，但如果有频繁请求的项目中，就会有性能问题
# 通过使用连接池技术，管理来进行优化，DBUnitls是一套Python的数据库连接池包，对链接对象进行自动链接和释放，提高高频高并发下数据访问性能
from configs import format
from configs import config
import pymysql.cursors

# 使用数据库连接池的方式链接数据库，提高资源利用率
pool = PooledDB(pymysql, mincached=2, maxcached=5, host=config.MYSQL_HOST, port=config.MYSQL_PORT,
                user=config.MYSQL_USER, passwd=config.MYSQL_PASSWORD, database=config.MYSQL_DATABASE,
                cursorclass=pymysql.cursors.DictCursor)
# mincached ：启动时开启的空的连接数量 ; maxcached ：连接池最大可用连接数量

app_application = Blueprint("app_application", __name__)


# 实现所属分类查询用于条件筛选
@app_application.route("/api/application/product", methods=['GET'])
def getProduct():
    # 使用连接池链接数据库
    connection = pool.connection()

    with connection.cursor() as cursor:
        # 查询产品信息表-按更新时间新旧排序
        sql = "SELECT id,keyCode,title FROM `products` WHERE `status`=0 ORDER BY `id` ASC"
        cursor.execute(sql)
        data = cursor.fetchall()

    # 按返回模版格式进行json结果返回
    response = format.resp_format_success
    response['data'] = data
    return response


#  实现分页查询应用,需要对查询条件进行按需拼接，还需要通过两次查询，一次查询总数量，一次是limit分页查询
@app_application.route("/api/application/search", methods=['POST'])
def searchBykey():
    body = request.get_data()
    body = json.loads(body)

    # 基础语句定义
    sql = ""

    # 获取pageSize和
    pageSize = 10 if body['pageSize'] is None else body['pageSize']
    currentPage = 1 if body['currentPage'] is None else body['currentPage']

    # 拼接查询条件
    if 'id' in body and body['id'] != '':
        sql = sql + " AND `id` = '{}'".format(body['id'])
    if 'title' in body and body['title'] != '':
        sql = sql + " AND `title` LIKE '%{}%'".format(body['title'])
    if 'keyCode' in body and body['keyCode'] != '':
        sql = sql + " AND `keyCode` LIKE '%{}%'".format(body['keyCode'])

    # 排序和页数拼接
    sql = sql + ' ORDER BY `update` ASC LIMIT {},{}'.format((currentPage - 1) * pageSize, pageSize)
    print(sql)

    # 使用连接池链接数据库
    connection = pool.connection()

    with connection:
        # 先查询总数
        with connection.cursor() as cursor:
            cursor.execute('SELECT COUNT(*) as `count` FROM `products` WHERE `status`=0' + sql)
            total = cursor.fetchall()

        # 执行查询
        with connection.cursor() as cursor:
            # 按照条件进行查询
            cursor.execute(
                'SELECT P.title FROM products AS P WHERE P.id = P.id and P.`status`=0' + sql)
            data = cursor.fetchall()

    # 按分页模版返回查询数据
    response = format.resp_format_success
    response['data'] = data
    response['total'] = total[0]['count']
    return response
