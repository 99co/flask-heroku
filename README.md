# Flask Boilerplate

## Introduction
This project serves as a quickstart for a Flask project. It also is compatible with Heroku, so you can deploy it directly, or run it standalone in your own set up

## Structure

    .
    ├── acme/
    │   ├── widget/
    │   │   ├── __init__.py
    │   │   ├── views.py
    │   ├── db.py
    │   ├── decorators.py
    │   ├── __init__.py
    │   ├── settings.py
    ├── __init__.py
    ├── main.py
    ├── Procfile
    └── requirements.txt


  The structure of the project is based off a single Flask app in a package (`acme/`) and a single Blueprint (`acme/widget/`)


## Settings
 The settings file (found in `acme/settings.py`) is classed-based. The variable `settings.CONFIG` is automatically set to eithe `DevConfig` or `ProductionConfig`, depending on whether the envvar `PRODUCTION` is set or not. If it is set, `settings.CONFIG` points to `ProductionConfig`. Otherwise, it points to `DevConfig`.

     CONFIG = ProductionConfig if bool(os.getenv("PRODUCTION", False)) else DevConfig

 While configuration options can be set in `settings.py`, there sometimes arises occasions where overriding the defaults with envvars is desirable. To account for this, the Config objects check for any set envvars that match their own keys, and take on the value set in the envvar.

 The Config objects also write their own configuration into `os.environ`, in order to provide for modules that insist on reading envvars instead of from a configuration file/object. The **exception** to this rule is the `PRODUCTION` key, which is never written back to the environment. This means that `os.getenv('PRODUCTION')` is always authoritative, and has to be set by the user.

         for k in dir(self):
            if k.isupper():
                if os.getenv(k):
                    setattr(self, k, os.getenv(k))
                if k != 'PRODUCTION':
                    os.environ[k] = str(getattr(self, k))


### Global configuration
A common idiom in Flask is to support app-wide config settings via `app.config` after initialising it via `app.config.from_object(settings.CONFIG)` or similar. However, this means that any other module that requires access the application configuration settings needs to import `app`, which may be bloated, or have side-effects.

Hence, this boilerplate provides `settings.CONFIG`. As mentioned above, `settings.CONFIG` encapsulates all appropriate application settings (depending on if the app is in `PRODUCTION` mode or not). Once imported `settings.CONFIG` can be used like a dictionary, eg.

    import settings
    database_uri = settings.CONFIG['DB_URI']
    welcome_msg = settings.CONFIG.get('WELCOME_MSG', 'Welcome to Acme Widgets')



# Contributing
Thanks for reading so far! If you're using this boilerplate and run into bugs/problems, feel free to create an issue and we'll look into it. Pull requests are welcome too!
