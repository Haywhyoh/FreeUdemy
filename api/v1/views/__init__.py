#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.all_courses import *
from api.v1.views.design import *
from api.v1.views.development import *
from api.v1.views.finance import *
from api.v1.views.health import *
from api.v1.views.software import *