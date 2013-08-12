import json
import datetime
from collections import defaultdict

from flask import current_app as app
from flask import request
from flask import session
from flask import jsonify
from flask import render_template
from flask.views import MethodView

import db
from decorators import crossdomain

class WidgetAPI(MethodView):

    decorators = [crossdomain(origin="*", methods=['POST'], headers=['content-type'])]

    def get(self):
        return "GET"

    def post(self):
        return "POST"
