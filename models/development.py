from models.engine.db_storage import DBStorage as freeudemydb
from pprint import pprint as printt

db = freeudemydb()
file = "../models/development.json"
development = db.create_collection(db_collection = "development")
db.dump_json_file(filename=file, collection=development)