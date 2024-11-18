from flask import Flask
from user import user_blueprint
from flask_cors import CORS

app = Flask(__name__)

# Set a secure secret key for session handling
app.secret_key = 'your_secret_key'

# Enable CORS with support for credentials
CORS(app, supports_credentials=True)

# Register the user blueprint
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
