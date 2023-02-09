#!/usr/bin/python3
import pymongo
import json
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    created_at = datetime.utcnow
    updated_at = datetime.utcnow