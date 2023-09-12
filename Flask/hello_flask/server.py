from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__) 
# Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html") 
    
# import statements, maybe some other routes
    
@app.route('/success')
def success():
    return "success"
    
@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/hi')
def ind():
    return render_template("hi.html", phrase="hello", times=5)

# app.run(debug=True) should be the very last statement! 

# Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=8000)    # Run the app in debug mode.

