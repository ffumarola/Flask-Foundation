#! ../env/bin/python
import os

from flask import Flask
from webassets.loaders import PythonLoader as PythonAssetsLoader

from appname import assets
from appname.models import db

from appname.extensions import (
    cache,
    assets_env,
    debug_toolbar,
    login_manager
)


def create_app(object_name, env="prod"):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. appname.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """

    app = Flask(__name__)

    app.config.from_object(object_name)
    app.config['ENV'] = env

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    
    return app


def register_extensions(app):
    # init the cache
    cache.init_app(app)
    # init debug toolbar
    debug_toolbar.init_app(app)
    # init SQLAlchemy
    db.init_app(app)
    # init login manager
    login_manager.init_app(app)
    # Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().iteritems():
        assets_env.register(name, bundle)


def register_blueprints(app):
    # register our blueprints
    from controllers.main import main
    app.register_blueprint(main)


def register_errorhandlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template("errors/{0}.html".format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)


if __name__ == '__main__':
    # Import the config for the proper environment using the
    # shell var APPNAME_ENV
    env = os.environ.get('APPNAME_ENV', 'prod')
    app = create_app('appname.settings.%sConfig' % env.capitalize(), env=env)

    app.run()
