from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from app import create_app
from app.models import db

# Load environment variables from .env file
load_dotenv()

app = create_app()


if __name__ == '__main__':
    port = int(os.getenv('SERVICE_PORT', 5001))
    if app.config["ENV"] == "development":
        with app.app_context():
            db.create_all()
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])