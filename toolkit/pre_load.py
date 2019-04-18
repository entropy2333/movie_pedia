# -*- coding: utf-8 -*-
import csv
import sys
import os
sys.path.append("..")

from Model.neo_models import Neo4j 
# from Model.mongo_model import Mongo
from toolkit.tree_API import TREE

# 预加载neo4j
neo_con = Neo4j()
neo_con.connectDB()
print('neo4j connected!')

# 读取电影层次树
filePath = os.getcwd()
tree = TREE()
tree.read_edge(filePath+'\\toolkit\movie_tree.txt')
tree.read_leaf(filePath+'\\toolkit\leaf.txt')

# # 预加载mongodb
# mongo = Mongo()
# mongo.makeConnection()
# print("mongodb connected")

# # 连接数据库
# mongodb = mongo.getDatabase("agricultureKnowledgeGraph")
# print("connect to agricultureKnowledgeGraph")

# # 得到collection
# collection = mongo.getCollection("train_data")
# print("get connection train_data")

# testDataCollection = mongo.getCollection("test_data")
# print("get connection test_data")