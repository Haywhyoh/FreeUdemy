from flask_login import UserMixin
from models.engine.db_storage import DBStorage
db = DBStorage()
users = db.create_collection("users")

class User(UserMixin):
    pass
