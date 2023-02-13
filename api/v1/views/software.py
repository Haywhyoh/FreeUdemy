from flask import jsonify, make_response, abort
import json
from api.v1.views import app_views
from flask import jsonify
from models.engine.db_storage import DBStorage
from models.engine.db_storage import freeudemydb
from bson.json_util import dumps
storage = DBStorage()
courses = freeudemydb["software"]

@app_views.route('software/', defaults={ 'page_num': None })
@app_views.route('software/<page_num>/', methods=['GET'], strict_slashes=False)
def get_all_soft_course(page_num):
    if page_num is None:
        page_num = 1
    page_num = int(page_num)
    data = storage.all(courses, page_num)
    return jsonify(data)

@app_views.route('software/<title>', defaults={ 'page_num': None })
@app_views.route('software/<title>/<page_num>/', methods=['GET'], strict_slashes=False)
def get_soft_by_title(title, page_num):
    if page_num is None:
        page_num = 1
    page_num = int(page_num)
    course = storage.get_by_title(title, courses)
    print(course)
    return jsonify(course)

@app_views.route('software/<course_id>/', methods=['DELETE'], strict_slashes=False)
def delete_soft_course():
    course = storage.get_by_id(id, courses)
    if not course:
        abort(404)


