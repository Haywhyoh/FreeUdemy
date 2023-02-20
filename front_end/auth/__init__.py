from flask import Blueprint

auth = Blueprint("auth", __name__)

from api.v1.views.index import *
from api.v1.views.all_courses import *
from api.v1.views.design import *
from api.v1.views.development import *
from api.v1.views.finance import *
from api.v1.views.health import *
from api.v1.views.software import *