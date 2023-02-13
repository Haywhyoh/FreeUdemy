from engine.db_storage import DBStorage as freeudemydb
from pprint import pprint as printt

db = freeudemydb()
file = "../models/software.json"
software = db.create_collection(db_collection = "software")
db.dump_json_file(filename=file, collection=software)