from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def level_1():
    return render_template('index.html', box_color= "aqua", numBoxes= 3)
    #two variables that will change in upcoming routes are the color and number of boxes
    #so those are the variables needed in return
    # most fixed level, nothing is being manipulated

@app.route('/play/<int:numBoxes>')
def level_2(numBoxes):
    return render_template('index.html', box_color= "aqua", numBoxes= numBoxes)
    # here we're playing with the number of boxes but keeping the color the same as level1
    #cant just say numBoxes in route; change string to int
    # example: http://localhost:8001/play/25 gives me 25 aqua boxes

@app.route('/play/<int:numBoxes>/<string:box_color>')
def level_3(numBoxes, box_color):
    return render_template('index.html', box_color= box_color, numBoxes= numBoxes)
    # here we are manipulating color AND number of boxes
    # write int same as level2;
    # string for box color as shown in platform video
    # example: http://localhost:8001/play/10/purple gives me 10 purple boxes

if __name__=="__main__":
    app.run(debug=True, port=8001)