import pymongo
import json
import pprint

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
freeudemydb = myclient["freeudemy_database"]
courses = freeudemydb["courses"]
dev = freeudemydb["development"]
des = freeudemydb["design"]
de2 = freeudemydb["devlopement"]
hel = freeudemydb["health"]
def create_collection(collection):
    collection = freeudemydb[collection]
    return collection

def dump_json_file(filename):
    with open(filename) as file:
        file_data = json.load(file)
        file_data = file_data["results"]
    if isinstance(file_data, list):
        courses.insert_many(file_data)
    else:
        courses.insert_one(file_data)
    return (True)

def dump_json_data():
    file_data = json.loads()
    if isinstance(file_data, list):
        courses.insert_many(file_data)
    else:
        courses.insert_one(file_data)
    return (True)

def get_by_title(query):
    myquery = { "title" : {"$regex": "/\b{}\b/i".format(query)}}
    course_list = courses.find(myquery)
    return course_list

def get_free():
    myquery = { "is_paid" : False}
    course_list = courses.find(myquery)
    return course_list

def get_paid():
    myquery = { "is_paid" : False}
    course_list = courses.find(myquery)
    return course_list

def delete_by_title(course_title):
    myquery = { "title" : course_title}
    courses.delete_one(myquery)
    return courses

def update_course(old_data, new_data):
    myquery = old_data
    update_val = { "$set" : new_data }
    return courses
print(freeudemydb.list_collection_names())
