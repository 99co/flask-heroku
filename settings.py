
import os

SECRET_KEY = '####SOME_SECRET_KEY_HERE####'
DEBUG = bool(os.getenv("DEBUG", False))
DB_URI = os.getenv("DB_URI", "mongodb://localhost/db")
