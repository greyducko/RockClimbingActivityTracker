# Group 8 Charles Loughin, Harvey Ng
# This module adapted from starter code: https://github.com/osu-cs340-ecampus/flask-starter-app/ (Authors: Michael Curry, Andrew Kamand, @mlapresta (on github)) 
# Code adapted: function to query database; request.method
# Date: 3/18/2024
# Flask blueprint and blueprint.route code adapted from: https://realpython.com/flask-blueprint/
# Original work: SQL queries; form inputs


from flask import Blueprint, request, render_template, redirect
from database.db_connector import query_db

# Create blueprint so routes in this module can be accessed from app.py
gyms_blueprint = Blueprint("gyms_blueprint", __name__)

# Route handles read and insert for gyms entity
@gyms_blueprint.route("/gyms", methods = ["POST", "GET"])
def gyms():

    if request.method == "GET":

        # Query to read gyms table
        query = "SELECT gym_id, gym_name FROM gyms;"
        results = query_db(query)

        return render_template("gyms.j2", gyms=results)
    
    if request.method == "POST":
        if request.form.get("add_gyms"):
            gym_name = request.form["gym_name"]

            # Query to insert gym
            query = "INSERT INTO gyms (gym_name) VALUE (%s);"
            query_db(query, query_params=(gym_name,))
            
            return redirect("/gyms")

# Route handles edit for gyms entity
@gyms_blueprint.route("/edit_gyms/<int:id>", methods=["POST", "GET"])
def edit_gyms(id):

    if request.method == "GET":

        # Query to get gym_name to prepopulate field
        query = "SELECT gym_id, gym_name FROM gyms WHERE gym_id = %s;"
        results = query_db(query, query_params=(id,))

        return render_template("edit_gyms.j2", results=results)
    
    if request.method == "POST":
            if request.form.get("edit_gyms"):

                gym_name = request.form["gym_name"]

                # Query to update gym
                query = "UPDATE gyms SET gym_name = %s WHERE gym_id = %s;"
                query_db(query=query, query_params=(gym_name, id))

            return redirect("/gyms")

