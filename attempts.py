# Group 8 Charles Loughin, Harvey Ng
# This module adapted from starter code: https://github.com/osu-cs340-ecampus/flask-starter-app/ (Authors: Michael Curry, Andrew Kamand, @mlapresta (on github)) 
# Code adapted: function to query database; request.method
# Date: 3/18/2024
# Flask blueprint and blueprint.route code adapted from: https://realpython.com/flask-blueprint/
# Original work: SQL queries; form inputs

from flask import Blueprint, request, render_template, redirect
from database.db_connector import query_db

# Create blueprint so routes in this module can be accessed from app.py
attempts_blueprint = Blueprint("attempts_blueprint", __name__)

# Route handles read and insert for attempts entity
@attempts_blueprint.route("/attempts", methods = ["POST", "GET"])
def attempts():

    if request.method == "GET":

        # Query to read attempts table
        query = "SELECT attempt_id, grade, is_success, attempts.session_id, sessions.date AS session_date FROM attempts INNER JOIN sessions ON attempts.session_id = sessions.session_id;"

        results = query_db(query)

        # Query to create dropdown of session_id, session_date
        query2 = "SELECT sessions.session_id AS session_id, sessions.date AS session_date FROM sessions;"
        sessions_ids_dates = query_db(query2)

        return render_template("attempts.j2", attempts=results, sessions_ids_dates=sessions_ids_dates)
    
    if request.method == "POST":
        if request.form.get("add_attempts"):
            grade = request.form["grade"]
            is_success = request.form["is_success"]
            session_id = request.form["session_id"]

            # Query to insert attempt
            query = "INSERT INTO attempts (grade, is_success, session_id) VALUE (%s, %s,%s);"
            query_db(query, query_params=(grade, is_success, session_id))

            return redirect("/attempts")
    

