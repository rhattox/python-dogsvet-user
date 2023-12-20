from flask import Flask
import logging
from .route.user import user

app = Flask(__name__)

# Enable Logging
app.logger.setLevel(logging.DEBUG)

app.register_blueprint(user)


if __name__ == "__main__":
    app.run(debug=True)