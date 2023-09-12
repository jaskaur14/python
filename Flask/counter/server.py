from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret' # set a secret key for security purposes
# our index route will handle rendering our form
@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template("index.html")
    # renders each time you click on "click" box
    # also checks to see if key exists in session


# @app.route('/users', methods=['POST'])
# def create_user():
#     ...
#     session['username'] = request.form['name']
#     session['useremail'] = request.form['email']
#     return redirect('/show')

# @app.route('/show')
# def show_user():
#     return render_template(...

@app.route('/destroy_session')
def destroy_session():
    session.clear()		# clears all keys which in this case is the counts we've been keeping track of
    return redirect('/') 
# redirects us to 0 count 



if __name__ == "__main__":
    app.run(debug=True, port=8004)
