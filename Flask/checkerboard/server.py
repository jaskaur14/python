from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def board_one():
    return render_template("index.html", row=8, col=8, color_one='red', color_two='black')

@app.route('/<int:x>')
def board_two(x):
    return render_template("index.html", row=8, col=x, color_one='red', color_two='black')

@app.route('/<int:x>/<int:y>')
def board_three(x,y):
    return render_template("index.html", row=x, col=y, color_one='red', color_two='black')


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)
