from models import DBStorage as freeudemydb
from pprint import pprint as printt

db = freeudemydb()
design = db.create_collection(db_collection = "design")
file = "../models/design.json"
db.dump_json_file(filename=file, collection=design)

print(design .count_documents({}))