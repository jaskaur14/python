from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="Bob belly."

@app.route('/')
def index():
    return render_template(index.html)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)