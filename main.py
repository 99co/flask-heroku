
import os

from flask import Flask

import settings
import widget
import db

app = Flask(__name__)
app.config.from_object(settings)
app.db = db.DB(app.config['DB_URI'])

# Routes
# API Routes
widget_view = widget.views.WidgetAPI.as_view("widget_view")
app.add_url_rule("/widget/", view_func=collector_view, methods=['GET', 'POST'])

if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
