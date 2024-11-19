from flask import Flask
from flask_session import Session
from user import user_blueprint
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)

# Set a secret key for session
app.secret_key = 'your_secret_key'

# Flask-Session configuration
app.config['SESSION_TYPE'] = 'filesystem'  # Store session data in files
app.config['SESSION_PERMANENT'] = True  # Persistent session
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)  # Set session lifetime to 30 days
Session(app)

# Enable CORS
CORS(app, supports_credentials=True)

# Register the user blueprint
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
