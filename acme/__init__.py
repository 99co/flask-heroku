import os

from flask import Flask

import settings
import db

app = Flask(__name__)
app.config.from_object(settings.CONFIG)
app.db = db.DB(app.config['DB_URI'])

# Blueprints
for bp in settings.BLUEPRINTS:
    mod, sep, b = bp['name'].rpartition(".")
    m = __import__(mod, fromlist=[b])
    app.register_blueprint(getattr(m, b), url_prefix=bp['url_prefix'])



if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
