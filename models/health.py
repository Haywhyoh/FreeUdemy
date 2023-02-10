from engine.db_storage import DBStorage as freeudemydb
from pprint import pprint as printt

db = freeudemydb()
file = "../models/development.json"
health = db.create_collection(db_collection = "health")
db.dump_json_file(filename=file, collection=health)