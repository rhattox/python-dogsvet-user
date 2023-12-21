import logging
from flask import Flask
from .route.user import user
from .etc.load_env import load_database_environment_variables
from alembic.config import Config
from alembic import command
app = Flask(__name__)

# Enable Logging
app.logger.setLevel(logging.DEBUG)
load_database_environment_variables()
app.register_blueprint(user)

# Enable Migrations
alembic_cfg = Config("alembic.ini")
command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    app.run(debug=True)