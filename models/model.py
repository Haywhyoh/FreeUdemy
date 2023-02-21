import pymongo
from models import DBStorage
myclient = pymongo.MongoClient("mongodb+srv://haywhyoh:Mydreams@freeudemy.epriojq.mongodb.net/?retryWrites=true&w=majority")
freeudemydb = myclient["freeudemy"]
db = DBStorage()

def load_all_courses():
    file = "../models/data.json"
    courses = db.create_collection(db_collection = "courses")
    db.dump_json_file(filename=file, collection=courses)

def load_design_courses():
    file = "../models/design.json"
    design = db.create_collection(db_collection = "design")
    db.dump_json_file(filename=file, collection=design)

def load_dev_courses():
    file = "../models/development.json"
    development = db.create_collection(db_collection = "development")
    db.dump_json_file(filename=file, collection=development)

def load_finance_courses():
    file = "../models/finance.json"
    finance = db.create_collection(db_collection = "finance")
    db.dump_json_file(filename=file, collection=finance)

def load_health_courses():
    file = "../models/health.json"
    health = db.create_collection(db_collection = "health")
    db.dump_json_file(filename=file, collection=health)

def load_software_courses():
    file = "../models/software.json"
    software = db.create_collection(db_collection = "software")
    db.dump_json_file(filename=file, collection=software)

if __name__ == "__main__":
    load_all_courses()
    load_design_courses()
    load_dev_courses()
    load_finance_courses()
    load_health_courses()
    load_software_courses()