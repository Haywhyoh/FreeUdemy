from flask import jsonify, make_response, abort
import json
from api.v1.views import app_views
from flask import jsonify
from models.engine.db_storage import DBStorage
from models.engine.db_storage import freeudemydb
from bson.json_util import dumps
storage = DBStorage()
courses = freeudemydb["courses"]

@app_views.route('courses/all', methods=['GET'], strict_slashes=False)
def get_all_course():
    data = storage.all(courses)
    return jsonify(data)

@app_views.route('course/<title>', methods=['GET'], strict_slashes=False)
def get_by_title(title):
    course = storage.get_by_title(title, courses)
    print(course)
    return jsonify(course)

