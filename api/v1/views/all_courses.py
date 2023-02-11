from flask import jsonify, make_response, abort
import json
from api.v1.views import app_views
from flask import jsonify, request
from models.engine.db_storage import DBStorage
from models.engine.db_storage import freeudemydb
from bson.json_util import dumps
storage = DBStorage()


@app_views.route('courses/', defaults={ 'page_num': None })
@app_views.route('courses/<page_num>/', methods=['GET'], strict_slashes=False)
def get_all_course(page_num):
    category = request.args.get('categories')
    my_course = freeudemydb[category]
    if page_num is None:
        page_num = 1
    page_num = int(page_num)
    data = storage.all(my_course, page_num)
    return jsonify(data)

@app_views.route('courses/<title>', defaults={ 'page_num': None })
@app_views.route('course/<title>/<page_num>/', methods=['GET'], strict_slashes=False)
def get_by_title(title, page_num):
    category = request.args.get('categories')
    search_text = request.args.get('query')
    courses = freeudemydb[category]
    if page_num is None:
        page_num = 1
    page_num = int(page_num)
    course = storage.get_by_title(search_text, courses)
    return jsonify(course)

@app_views.route('courses/<course_id>/', methods=['DELETE'], strict_slashes=False)
def delete_course():
    category = request.args.get('categories')
    courses = freeudemydb[category]
    course = storage.get_by_id(id, courses)
    if not course:
        abort(404)


