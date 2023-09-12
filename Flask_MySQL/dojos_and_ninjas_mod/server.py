from flask_app import app
# ...server.py

from flask_app.controllers import ninjas, dojos
# ...server.py



if __name__ == "__main__":
    app.run(debug=True, host = "localhost", port = 8000)

