from flask import request
import json

from flask import Blueprint,request,jsonify
from py2neo import Graph,NodeMatcher,cypher,Node,Relationship,RelationshipMatcher
import requests
from requests.auth import HTTPBasicAuth

app_neo4j = Blueprint("app_neo4j", __name__)
graphDB = Graph('bolt://0.0.0.0:7687', auth=('neo4j', 'neo4j')
header = {
    "content-type":'application/json'
}
}
def joltAPI(user_query):
    data = {
        "statements" : [{
            "statement": user_query
        }]
    }
    # database authentication
    data = graphDB.run(user_query).data()
    idList = []
    nodes = []
    links = []
    linkID = []
    for item in data:
        print(item['p'].start_node, item['p'].end_node)
        if item['p'].start_node.identity not in idList:
            node = {}
            idList.append(item['p'].start_node.identity)
            node['id'] = item['p'].start_node.identity
            node['label'] = str(item['p'].start_node.labels).replace(':','').strip()
            node['properties'] = dict(item['p'].start_node)
            nodes.append(node)
        if item['p'].end_node.identity not in idList:
            node = {}
            idList.append(item['p'].end_node.identity)
            node['id'] = item['p'].end_node.identity
            node['label'] = str(item['p'].end_node.labels).replace(':', '').strip()
            node['properties'] = dict(item['p'].end_node)
            nodes.append(node)

        for rel in item['p'].relationships:
            print(rel)
            if rel.identity in linkID:
                continue
            linkID.append(rel.identity)
            link = {}
            for source in nodes:
                if source['id'] == rel.start_node.identity:
                    link['source'] = source
                if source['id'] == rel.end_node.identity:
                    link['target'] = source
            link['id'] = rel.identity
            link['properties'] = dict(rel)
            link['type'] = type(rel).__name__
            links.append(link)
            # print(rel.start_node)
            # print(rel.end_node)
            # print(rel.identity)
            # print(dict(rel))
            # print(type(rel).__name__)
        # print(nodes)
        # print(links)
    return nodes,links
        # print(item['p'].start_node.identity)
        # print(item['p'].start_node.labels)
        # print(dict(item['p'].start_node))

        # print(item['p'].end_node)
        # print(item['p'].relationships)


# data = joltAPI('MATCH p=()-[r:contain]->() RETURN p')
#     res = requests.post(url='http://localhost:7474/db/data/transaction/commit', data=json.dumps(data), headers=header, auth=HTTPBasicAuth('neo4j', '123456'))
#     # initialize return data
#     all_data = json.loads(res.text)['results']
#
#     return_data = {}
#     nodes = []
#     links = []
#     # iterate all data
#     for item in all_data:
#         if len(item['data']):
#             for item1 in item['data']:
#                 # array mapping
#                 if len(item1['row']) > 0:
#                     if type(item1['row'][0]).__name__ == 'list':
#                         for row, meta in zip(item1['row'], item1['meta']):
#                             link = {}
#                             node = {}
#                             # element mapping
#                             for (rowItem, metaItem) in zip(row, meta):
#                                 if metaItem['type'] == 'node':
#                                     # property merge
#                                     node['properties'] = {**rowItem}
#                                     node = {**node, **metaItem}
#                                     # node = {**rowItem, **metaItem}
#                                 if metaItem['type'] == 'relationship':
#                                     rel_property = {**rowItem, **metaItem}
#                                 nodes.append(node)
#                             if len(meta) > 1:
#                                 link['source'] = meta[0]['id']
#                                 link['target'] = meta[2]['id']
#                                 links.append(link)
#                             link['property'] = rel_property
#                     elif type(item1['row'][0]).__name__ == 'dict':
#                         link = {}
#                         node = {}
#                         rel_property = {}
#                         for row, meta in zip(item1['row'], item1['meta']):
#                             if meta['type'] == 'node':
#                                 # property merge
#                                 node['properties'] = {**row}
#                                 node = {**node, **meta}
#                             if meta['type'] == 'relationship':
#                                 rel_property = {**row, **meta}
#                                 link['property'] = rel_property
#                                 rel = graphDB.relationships.get(rel_property['id'])
#                                 nodes.append({
#                                     'id': rel.start_node.identity,
#                                     'type': 'node',
#                                     **dict(rel.start_node)
#                                 })
#                                 nodes.append({
#                                     'id': rel.end_node.identity,
#                                     'type': 'node',
#                                     **dict(rel.end_node)
#                                 })
#                                 # print('start_node',rel.start_node,dict(rel.start_node))
#                                 # print('end_node',rel.end_node)
#                                 link['source'] = rel.start_node.identity
#                                 link['target'] = rel.end_node.identity
#                                 links.append(link)
#                             nodes.append(node)
#                         # if len(item1['meta']) > 1:
#                         #     link['source'] = item1['meta'][0]['id']
#                         #     link['target'] = item1['meta'][2]['id']
#                         #     links.append(link)
#                         # link['property'] = rel_property
#     # -------------------
#     for item in nodes:
#         # print(item['id'])
#         node_data = graphDB.nodes.get(item['id'])
#         # print(node_data)
#         # print(help(node_data))
#         labels = set(node_data.labels)
#         # print(type(node_data.labels) ,node_data.labels)
#         # print(list(labels) )
#
#         item['label'] = labels[0]
#
#
#
#
#     for item in links:
#         # print('link',item['property']['id'])
#         link_data = graphDB.relationships.get(item['property']['id'])
#         # labels = set(link_data.labels)
#         # print('linkdata',type(link_data).__name__ )
#         # # print(type(node_data.labels) ,node_data.labels)
#         # print(list(labels) )
#         item['label'] = type(link_data).__name__
#     # -------------------
#     # print("\n")
#     # print(nodes,links)
#     # empty data handling
#
#     # remove duplicate nodes
#     id_list = []
#     node_list = []
#     for node in nodes:
#         if node['id'] not in id_list:
#             # print(node['id'])
#             node_list.append(node)
#             id_list.append(node['id'])
#
#     return_data['nodes'] = node_list
#     return_data['links'] = links
#
#     if len(nodes) == 0 and len(links) == 0:
#         return {'status': 'empty_data'}
#     else:
#         return return_data
#
#
#
#     # if len(nodes) == 0 and len(links) == 0:
#     #     return {'status':'empty_data'}
#     # else:
#     #     return 'return_data'
#
@app_neo4j.route("/api/neo4j/getAllData", methods=['GET'])
def getAllData():
    # 按返回模版格式进行json结果返回
    resp_data = {
        "code": 20000,
        "message": "success",
        "data": {}
    }
    if request.method != 'GET':
        resp_data['message'] = '请求方法出错'
        return resp_data
    name = request.args.get('name')
    num = request.args.get('num')
    print(num)
    if num == None:
        num = ''
    nodes,links = joltAPI("MATCH p=(n:subject{name:'%s'})-[r*1..%s]->() RETURN p" % (name,num))
    print("MATCH p=(n:subject{name:'%s'})-[r*1..%s]->() RETURN p" % (name,num))
    resp_data['data']['nodes'] = nodes
    resp_data['data']['links'] = links
    # 获取请求传递json
    # print(data)
    return resp_data
@app_neo4j.route("/api/neo4j/deletenode", methods=['GET'])
def deleteNode():
    resp_data = {
        "code": 20000,
        "message": "success",
        "data": {}
    }
    if request.method != 'GET':
        resp_data['message'] = '请求方法出错'
        return resp_data
    print(request.args.get('id'))
    id = request.args.get('id')
    try:
        node = graphDB.evaluate("MATCH (n) WHERE id(n) = {} RETURN n".format(id))
        graphDB.delete(node)
        return resp_data
    except Exception as e:
        resp_data['code'] = 400
        resp_data['message'] = 'error'
        return resp_data
@app_neo4j.route("/api/neo4j/addnode", methods=['POST'])
def addNode():
    resp_data = {
        "code": 20000,
        "message": "success",
        "data": {}
    }
    if request.method != 'POST':
        resp_data['message'] = '请求方法出错'
        return resp_data
    data = request.get_data()  # 获取post请求body数据
    data = json.loads(data)  # 将字符串转成json
    print(data)
    source_node = graphDB.run(f'match (n) where id(n)={data["parentID"]} return n').data()[0]['n']
    del data['parentID']
    relationShip = data['relationship']
    del data['relationship']
    print(source_node)
    target_node = Node()
    for (key, value) in zip(data.keys(), data.values()):
        if key == 'label':
            target_node.add_label(value)
        else:
            target_node[key] = value
    graphDB.create(target_node)
    rel = Relationship(source_node, relationShip, target_node)
    graphDB.create(rel)
    return resp_data
