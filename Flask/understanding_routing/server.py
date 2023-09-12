from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"Hello World!"

@app.route("/dojo")
def dojo():
    return f"Dojo!"

@app.route('/say/<name>')
def hi(name):
    print(name)
    return f"Hi {name}"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return f"{word * num}"

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)