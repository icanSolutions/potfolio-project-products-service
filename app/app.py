from flask import Flask, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Config from environment variables
app.config['ENV'] = os.getenv('FLASK_ENV', 'production')
app.config['DEBUG'] = os.getenv('DEBUG', 'false').lower() == 'true'

if __name__ == '__main__':
    port = int(os.getenv('SERVICE_PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])