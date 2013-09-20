
__all__ = ['views']

from flask import Blueprint

import views

widgets = Blueprint('widgets', __name__, static_folder='static', template_folder='templates')

# Routes
# API Routes
widget_view = views.WidgetAPI.as_view("widget_view")
widgets.add_url_rule("/widget/", view_func=widget_view, methods=['GET', 'POST'])
