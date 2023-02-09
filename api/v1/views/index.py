#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
from models.engine.db_storage import DBStorage
from models.design import design as Design
from models.development import development as Development
from models.all_courses import courses as Courses

storage = DBStorage()

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    categories = ["Courses", "Business", "Design", "Development", "Finance & Accounting",
                    "Health & Fitness", "IT & Software", "Lifestyle", 
                    "Marketing", "Music", "Office", "Productivity", "Personal Development",
                    "Photography & Video", "Teaching & Academics"]
    names = ["courses", "business", "design", "development", "finance & accounting",
                    "health & Fitness", "iT & software", "lifestyle", 
                    "marketing", "music", "office", "productivity", "personal development",
                    "photography & video", "teaching & academics"]

    num_objs = {}
    for i in range(len(categories)):
        num_objs[names[i]] = storage.count(categories[i])

    return jsonify(num_objs)