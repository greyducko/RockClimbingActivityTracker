# Group 8 Charles Loughin, Harvey Ng
# This module adapted from starter code: https://github.com/osu-cs340-ecampus/flask-starter-app/ (Authors: Michael Curry, Andrew Kamand, @mlapresta (on github)) 
# Code adapted: function to define routes
# Date: 3/18/2024
# Flask register_blueprint code adapted from: https://realpython.com/flask-blueprint/

from flask import Flask, render_template
from users_gyms import users_gyms_blueprint
from users import users_blueprint
from gyms import gyms_blueprint
from attempts import attempts_blueprint
from sessions import sessions_blueprint

app = Flask(__name__)

# Routes 
@app.route('/')
def root():
    return render_template("index.j2")

# Flask blueprint used to modularize code into separate files
# Register blueprints so the routes in each file can be accessed
app.register_blueprint(users_gyms_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(gyms_blueprint)
app.register_blueprint(attempts_blueprint)
app.register_blueprint(sessions_blueprint)

if __name__ == "__main__":
    app.run(port=4438, debug=True) 