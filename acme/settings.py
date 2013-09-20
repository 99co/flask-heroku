
import os


class ConfigMeta(type):

    def __getitem__(self, key):
        # Implementing __getitem__() allows us to use dict key indexing
        # syntax on the Config objects
        return self.__dict__[key]


class DevConfig(object):

    __metaclass__ = ConfigMeta

    SECRET_KEY = '####SOME_SECRET_KEY_HERE####'
    DEBUG = True
    DB_URI = "mongodb://localhost/db"


    @classmethod
    def read_env(self):

        # For every uppercase key in the Config object,
        # check for an equivalent envvar. If the envvar is set, take
        # it's value instead
        for k in dir(self):
            if k.isupper():
                if os.getenv(k):
                    setattr(self, k, os.getenv(k))

                # Write all keys except 'PRODUCTION' back into the environment
                # so that they are accessible to modules who insist on
                # using os.getenv instead of our global config
                # We don't write PRODUCTION back to the environment so that we
                # can use that as the single authoritative source of which mode
                # we're in
                if k != 'PRODUCTION':
                    os.environ[k] = str(getattr(self, k))

        return self


    @classmethod
    def get(self, key, default=None):
        # Implementing get() allows us to use the Config objects in the
        # same way we use dicts, eg.
        # somevar = obj.get('key', 'default_value')
        try:
            return getattr(self, key)
        except AttributeError as e:
            return default


class ProductionConfig(DevConfig):

    DEBUG = False
    DB_URI = "mongodb://username:password@remotehost:9999/db"


class TestConfig(DevConfig):
    pass


BLUEPRINTS = (
              {"name": "acme.widget.widgets", "url_prefix": "/widgets"},
            )

# Here we bootstrap the Config object, choosing one depending if we should be
# in PRODUCTION mode or not.
# This is followed by overriding set values with those set as envvars via
# read_env(), allowing for dynamic configuration in environments like Heroku
CONFIG = ProductionConfig if bool(os.getenv("PRODUCTION", False)) else DevConfig
CONFIG.read_env()
