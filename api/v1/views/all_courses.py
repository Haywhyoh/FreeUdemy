from flask import jsonify, make_response, abort
from api.v1.views import app_views
from flask import jsonify, request
from models.engine.db_storage import DBStorage
from models import freeudemydb
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from models import users
from bson.json_util import dumps


storage = DBStorage()
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = storage.get_user(users, username)
    if username == user["username"] and check_password_hash(user["password"], password):
        return username

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
def get_by_search(title, page_num):
    category = request.args.get('categories')
    search_text = request.args.get('query')
    courses = freeudemydb[category]
    if page_num is None:
        page_num = 1
    page_num = int(page_num)
    course = storage.get_by_search(search_text, courses)
    return jsonify(course)

@app_views.route('courses_add/', methods=["POST"], strict_slashes=False)
@auth.login_required
def add_course():
    title = request.form.get("title")
    instructor = request.form.get("instructor")
    course_link = request.form.get("url")
    image_url = request.form.get("image_url")
    reviews = request.form.get("reviews")
    price = request.form.get("price")
    category = request.form.get("category")
    courses = freeudemydb[category]
    added_course = storage.add_course(courses, title=title, price=price, images=image_url, url=course_link, reviews=reviews, instructor=instructor, category=category)
    return "Hello, {} {}!".format(auth.current_user(), added_course)

@app_views.route('courses/', methods=['DELETE'], strict_slashes=False)
@auth.login_required
def delete_course():
    category = request.form.get('category')
    title = request.form.get('title')
    courses = freeudemydb[category]
    course = storage.delete_by_title(title, courses)
    if not course:
        abort(404)
    return make_response("Deleted succesfully", 200)