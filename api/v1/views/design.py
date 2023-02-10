from flask import jsonify, make_response, abort
import json
from api.v1.views import app_views
from flask import jsonify
from models.engine.db_storage import DBStorage
from models.engine.db_storage import freeudemydb
from bson.json_util import dumps
storage = DBStorage()
courses = freeudemydb["design"]

@app_views.route('design/', methods=['GET'], strict_slashes=False)
def get_design_course():
    data = storage.all(courses)
    return jsonify(data)

@app_views.route('design/<title>', methods=['GET'], strict_slashes=False)
def get_des_by_title(title):
    course = storage.get_by_title(title, courses)
    print(course)
    return jsonify(course)

@app_views.route('design/<course_id>', methods=['DELETE'], strict_slashes=False)
def delete_des_course():
    course = storage.get_by_id(id, courses)
    if not course:
        abort(404)
