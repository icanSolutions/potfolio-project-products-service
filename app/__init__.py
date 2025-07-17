from flask import Flask
from .config import Config
from .models import db
from .routes import bp as routes_bp
from .errors import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(routes_bp)
    
    register_error_handlers(app)

    return app