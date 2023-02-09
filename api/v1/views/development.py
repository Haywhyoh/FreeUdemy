#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
from models.engine.db_storage import DBStorage
from models.engine.db_storage import freeudemydb
storage = DBStorage()