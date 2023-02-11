#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
from models.engine.db_storage import DBStorage
from models.engine.db_storage import freeudemydb
storage = DBStorage()
Courses = freeudemydb["courses"]
Development = freeudemydb["development"]
Design = freeudemydb["design"]
Finance = freeudemydb["finance"]
Software = freeudemydb["software"]
Health = freeudemydb["health"]

@app_views.route('/', methods=['GET'], strict_slashes=False)
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    categories = [Courses, Development, Design, Health, Finance, Software]
    names = ["courses", "business", "design", "development", "finance & accounting",
                    "health & Fitness", "iT & software", "lifestyle", 
                    "marketing", "music", "office", "productivity", "personal development",
                    "photography & video", "teaching & academics"]

    num_objs = {}
    for i in range(len(categories)):
        num_objs[names[i]] = storage.count(categories[i])

    return jsonify(num_objs)