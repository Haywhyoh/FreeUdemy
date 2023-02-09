from engine.db_storage import DBStorage as freeudemydb
from pprint import pprint as printt

db = freeudemydb()
file = "../models/data.json"
courses = db.create_collection(db_collection = "courses")
db.dump_json_file(filename=file, collection=courses)
