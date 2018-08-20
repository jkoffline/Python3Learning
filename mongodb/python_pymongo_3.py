#!/bin/python3
# -*- coding: utf-8 -*-
#
# 17 August, 2018
# Karl.Lv@outlook.com
#
# https://www.w3schools.com/python/python_mongodb_getstarted.asp


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one()

print(x)

print("====================")
for y in mycol.find():
    print(y)

print("====================")
for z in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(z)

print("====================")
for u in mycol.find({},{ "address": 0 }):
  print(u)

print("====================")
mydoc = mycol.find().sort("name")
for x in mydoc:
    print(x)

print("====================")
mydoc = mycol.find().sort("name", -1)
for x in mydoc:
    print(x)