from flask_app.controllers import users_plural
# ...server.py
from flask_app import app


if __name__=="__main__":
    app.run(debug=True, port=8011)