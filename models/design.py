from engine.db_storage import DBStorage as freeudemydb
from pprint import pprint as printt

db = freeudemydb()
file = "../models/design.json"
design = db.create_collection(db_collection = "design")
db.dump_json_file(filename=file, collection=design)