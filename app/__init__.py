from flask import Flask
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    csrf = CSRFProtect(app)

    from . import routes
    app.register_blueprint(routes.bp)

    return app
