#!/bin/python3
# -*- coding: utf-8 -*-
#
# August 16, 2018
# Karl.Lv@outlook.com


import datetime
import pprint
from  pymongo import MongoClient

client = MongoClient('localhost', 27017)


db = client['test-database']
print(client.list_database_names())

collection = db['test-database']
print(db.list_collection_names())

post = {"author": "Karl",
        "text": "WTF!",
        "tags": ["monogodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

print("========")
print(post_id)
print("========")

pprint.pprint(posts.find_one())