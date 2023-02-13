from engine.db_storage import DBStorage
db = DBStorage()
users = db.create_collection("users")