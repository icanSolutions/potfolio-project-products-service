from flask import Flask
from .config import config_by_name
from .models import db
from .routes import bp as routes_bp
from .errors import register_error_handlers
import os
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(
        app,
        supports_credentials=True,
        origins=["http://localhost:5173"]  # your frontend origin
    )
    env = os.getenv("FLASK_ENV", "production").lower()
    app.config.from_object(config_by_name[env])

    db.init_app(app)
    app.register_blueprint(routes_bp)
    
    register_error_handlers(app)

    return app