# Group 8 Charles Loughin, Harvey Ng
# This module adapted from starter code: https://github.com/osu-cs340-ecampus/flask-starter-app/ (Authors: Michael Curry, Andrew Kamand, @mlapresta (on github)) 
# Code adapted: function to query database; request.method
# Date: 3/18/2024
# Flask blueprint and blueprint.route code adapted from: https://realpython.com/flask-blueprint/
# Original work: SQL queries; form inputs


from flask import Blueprint, request, render_template, redirect
from database.db_connector import query_db

# Create blueprint so routes in this module can be accessed from app.py
sessions_blueprint = Blueprint("sessions_blueprint", __name__)

# Route handles read and insert for sessions entity
@sessions_blueprint.route("/sessions", methods = ["POST", "GET"])
def sessions():

    if request.method == "GET":
        
        # Query to read sessions table
        query = "SELECT session_id, date, first_name, last_name, gym_name FROM sessions INNER JOIN users ON sessions.user_id = users.user_id LEFT OUTER JOIN gyms ON sessions.gym_id = gyms.gym_id;"

        results = query_db(query)
        
        # Query to get all full names from users table to create dropdown when inserting new session
        query2 ="SELECT user_id, CONCAT(first_name, ' ', last_name) AS full_name FROM users;"
        full_names=query_db(query2)
        print(full_names)

        # Query to get all gym_names from gyms table to create dropwdown when inserting new session
        query3 ="SELECT gym_id, gym_name FROM gyms"
        gym_names=query_db(query3)

        return render_template("sessions.j2", sessions=results, full_names=full_names, gym_names=gym_names)
    
    if request.method == "POST":
        if request.form.get("add_sessions"):
            
            date = request.form["date"]
            user_id = request.form["user_id"]
            gym_id = request.form["gym_id"]
           
            # Query to insert into sessions table
            query = "INSERT INTO sessions (date, user_id, gym_id) VALUE (%s, %s,%s);"
            query_db(query, query_params=(date, user_id, gym_id))
            
            return redirect("/sessions")

# Route handles edit for sessions entity
@sessions_blueprint.route("/edit_sessions/<int:id>", methods=["POST", "GET"])
def edit_sessions(id):

    if request.method == "GET":

        # Query to prepopulate fields when editing a session
        query = "SELECT session_id, date, CONCAT(first_name,' ', last_name) AS full_name, gym_name FROM sessions INNER JOIN users ON sessions.user_id = users.user_id LEFT JOIN gyms ON sessions.gym_id = gyms.gym_id WHERE session_id = %s;"
        results = query_db(query, query_params=(id,))

        # Query to get all gym_names from gyms table to create dropdown when editing a session
        query2 = "SELECT gym_id, gym_name FROM gyms"
        gym_names = query_db(query2)
  
        return render_template("edit_sessions.j2", results=results, gym_names=gym_names)
    
    if request.method == "POST":
        if request.form.get("edit_sessions"):
    
            gym_id = request.form["gym_id"]

            if gym_id == "NULL":

                # Query to edit a session and give it a NULL gym_id
                query = "UPDATE sessions SET gym_id = NULL WHERE session_id = %s;"
                query_db(query=query, query_params=(id, ))

            else:

                # Query to edit a session and give it an existing gym_id
                query = "UPDATE sessions SET gym_id = %s WHERE session_id = %s;"
                query_db(query=query, query_params=(gym_id, id))

            return redirect("/sessions")


