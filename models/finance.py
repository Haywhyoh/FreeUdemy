from engine.db_storage import DBStorage as freeudemydb
from pprint import pprint as printt

db = freeudemydb()
file = "../models/finance.json"
finance = db.create_collection(db_collection = "finance")
db.dump_json_file(filename=file, collection=finance)