from flask import jsonify, make_response, abort
import json
from api.v1.views import app_views
from flask import jsonify
from models.engine.db_storage import DBStorage
from models.engine.db_storage import freeudemydb
from bson.json_util import dumps
storage = DBStorage()
courses = freeudemydb["development"]

@app_views.route('development/', methods=['GET'], strict_slashes=False)
def get_all_dev():
    data = storage.all(courses)
    return jsonify(data)

@app_views.route('development/<title>', methods=['GET'], strict_slashes=False)
def get_dev_by_title(title):
    course = storage.get_by_title(title, courses)
    print(course)
    return jsonify(course)

@app_views.route('development/<course_id>', methods=['DELETE'], strict_slashes=False)
def delete_dev_course():
    course = storage.get_by_id(id, courses)
    if not course:
        abort(404)
