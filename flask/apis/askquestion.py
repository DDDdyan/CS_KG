# -*- coding:utf-8 -*-

from flask import Blueprint

import pymysql.cursors
from flask import request
import json
from configs import config
from dbutils.pooled_db import PooledDB
import numpy as np
import re

app_askquestion = Blueprint("app_askquestion", __name__)
question = [
    {'question':'线性IR所在章节','answer':'第六章'},
    {'question':'流敏感分析的概念','answer':'概念'},
    {'question':'编译程序的工作过程','answer':'一般可划分为五个阶段:词法分析;语法分析;语义分析与中间代码生成;优化;目标代码生成'},
    {'question':'词法分析器的功能','answer':'输入源程序、输出单词符号'},
    {'question':'DFA与NFA区别','answer':'DFA:易于程序实现,仅有一个初态,箭弧上只有一个字符,单值部分映射,一一对应;NFA:易于人工设计，一或多个初态，箭弧上可以为一个字，映射多个状态。'},
    {'question':'静态分配策略(FORTRAN)','answer':'如果在编译时能确定数据空间的大小，则可采用静态分配方法：在编译时刻为每个数据项目确定出在运行时刻的存储空间中的位置'},
    {'question':'动态分配策略(PASCAL)','answer':'如果在编译时不能确定运行时数据空间的大小，则必须采用动态分配方法。允许递归过程和动态申请释放内存'},
]
def get_word_vector(s1, s2):
    """
    :param s1: 字符串1
    :param s2: 字符串2
    :return: 返回字符串切分后的向量
    """
    # 字符串中文按字分，英文按单词，数字按空格
    regEx = re.compile('[\\W]*')
    res = re.compile(r"([\u4e00-\u9fa5])")
    p1 = regEx.split(s1.lower())
    str1_list = []
    for str in p1:
        if res.split(str) == None:
            str1_list.append(str)
        else:
            ret = res.split(str)
            for ch in ret:
                str1_list.append(ch)
    # print(str1_list)
    p2 = regEx.split(s2.lower())
    str2_list = []
    for str in p2:
        if res.split(str) == None:
            str2_list.append(str)
        else:
            ret = res.split(str)
            for ch in ret:
                str2_list.append(ch)
    # print(str2_list)
    list_word1 = [w for w in str1_list if len(w.strip()) > 0]  # 去掉为空的字符
    list_word2 = [w for w in str2_list if len(w.strip()) > 0]  # 去掉为空的字符
    # 列出所有的词,取并集
    key_word = list(set(list_word1 + list_word2))
    # 给定形状和类型的用0填充的矩阵存储向量
    word_vector1 = np.zeros(len(key_word))
    word_vector2 = np.zeros(len(key_word))
    # 计算词频
    # 依次确定向量的每个位置的值
    for i in range(len(key_word)):
        # 遍历key_word中每个词在句子中的出现次数
        for j in range(len(list_word1)):
            if key_word[i] == list_word1[j]:
                word_vector1[i] += 1
        for k in range(len(list_word2)):
            if key_word[i] == list_word2[k]:
                word_vector2[i] += 1

    # 输出向量
    return word_vector1, word_vector2

def cos_dist(vec1, vec2):
    """
    :param vec1: 向量1
    :param vec2: 向量2
    :return: 返回两个向量的余弦相似度
    """
    dist1 = float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))
    return dist1


# 使用用户名密码创建数据库链接
# ​PyMySQL使用文档  https://pymysql.readthedocs.io
def connectDB():
    connection = pymysql.connect(host=config.MYSQL_HOST,   # 数据库IP地址或链接域名
                             user=config.MYSQL_USER,     # 设置的具有增改查权限的用户
                             password=config.MYSQL_PASSWORD, # 用户对应的密码
                             database=config.MYSQL_DATABASE,# 数据表
                             charset='utf8mb4',  # 字符编码
                             cursorclass=pymysql.cursors.DictCursor) # 结果作为字典返回游标
    # 返回新的书库链接对象
    return connection

# 搜索接口
@app_askquestion.route("/api/askquestion/getanswer",methods=['POST'])
def get_answer():
    # 获取请求传递json body
    body = request.get_data()
    askque = json.loads(body)['question']
    cos = 0
    answer = ''
    for item in question:
        v1, v2 = get_word_vector(item['question'], askque)

        if cos_dist(v1,v2) > cos:
            cos = cos_dist(v1,v2)
            answer = item['answer']
            print(cos,answer)
    if cos > 0.6:

        resp_data = {
            "code": 20000,
            "data": answer
        }

        return resp_data
    else:
        resp_data = {
            "code": 20000,
            "data": '暂无答案'
        }

        return resp_data



