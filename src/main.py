from flask import Flask
import logging
from .route.user import user
from .etc.load_env import load_database_environment_variables
app = Flask(__name__)

# Enable Migrations

# Enable Logging
app.logger.setLevel(logging.DEBUG)
load_database_environment_variables()
app.register_blueprint(user)


if __name__ == "__main__":
    app.run(debug=True)