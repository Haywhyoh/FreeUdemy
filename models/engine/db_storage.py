#!/usr/bin/python3
import pymongo
import json
import pprint
from datetime import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
freeudemydb = myclient["freeudemy_database"]
time = "%Y-%m-%dT%H:%M:%S.%f"
now = datetime.now()
class DBStorage:
    def __init__(self):
        pass

    def create_collection(self, db_collection):
        collection = freeudemydb[db_collection]
        return collection

    def dump_json_file(self, filename=None, collection=None):
        with open(filename) as file:
            file_data = json.load(file)
            file_data = file_data["results"]
            for i in file_data:
                i["created_at"] = now.strftime(time)
                i["updated_at"] = now.strftime(time)
        if isinstance(file_data, list):
            collection.insert_many(file_data)
        else:
            collection.insert_one(file_data)
        return (collection)
    
    def dump_json_data(self, file_data=None, collection=None):
        file_data = json.loads()
        for i in file_data:
                i["created_at"] = now.strftime(time)
                i["updated_at"] = now.strftime(time)
        if isinstance(file_data, list):
            collection.insert_many(file_data)
        else:
            collection.insert_one(file_data)
    
        return (collection)

    def get_by_title(self, query, collection):
        myquery = { "title" : {"$regex": "/\b{}\b/i".format(query)}}
        course_list = collection.find(myquery)
        return course_list

    def get_free(self, collection):
        myquery = { "is_paid" : False}
        course_list = collection.find(myquery)
        return course_list

    def get_paid(self, collection):
        myquery = { "is_paid" : False}
        course_list = collection.find(myquery)
        return course_list

    def delete_by_title(self, course_title, collection):
        myquery = { "title" : course_title}
        collection.delete_one(myquery)
        return collection

    def update_course(self, old_data, new_data, collection):
        new_data["updated_at"] = now.strftime(time)
        myquery = old_data
        update_val = { "$set" : new_data }
        return collection