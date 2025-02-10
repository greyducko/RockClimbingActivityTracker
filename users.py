# Group 8 Charles Loughin, Harvey Ng
# This module adapted from starter code: https://github.com/osu-cs340-ecampus/flask-starter-app/ (Authors: Michael Curry, Andrew Kamand, @mlapresta (on github)) 
# Code adapted: function to query database; request.method
# Date: 3/18/2024
# Flask blueprint and blueprint.route code adapted from: https://realpython.com/flask-blueprint/
# Original work: SQL queries; form inputs

from flask import Blueprint, request, render_template, redirect
from database.db_connector import query_db

# Create blueprint so routes in this module can be accessed from app.py
users_blueprint = Blueprint("users_blueprint", __name__)

# Route handles read and insert for users
@users_blueprint.route("/users", methods = ["POST", "GET"])
def users():

    if request.method == "GET":

        # Query to read users table
        query = "SELECT user_id, first_name, last_name, email, birth_date FROM users;"

        results = query_db(query)

        return render_template("users.j2", users=results)
    
    if request.method == "POST":
        if request.form.get("add_users"):
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            birth_date = request.form["birth_date"]

            try:

                # Query to insert into users table
                query = "INSERT INTO users (first_name, last_name, email, birth_date) VALUE (%s, %s,%s,%s);"
                query_db(query, query_params=(first_name, last_name, email, birth_date))
                
                return redirect("/users")
            
            except:

                # Return error if inserting an email that already exists

                return render_template("/users_error.j2")


# Route handles delete for users
@users_blueprint.route("/delete_users/<int:id>")
def delete_users(id):

    # Query to delete user
    query = "DELETE FROM users WHERE user_id = %s;"
    query_db(query=query, query_params=(id,))
            
    return redirect("/users")


# Route handles edit for users
@users_blueprint.route("/edit_users/<int:id>", methods=["POST", "GET"])
def edit_users(id):

    if request.method == "GET":
      
        # Query to get first_name, last_name, email, and birth_date of user being edited to prepopulate fields while editing users table
        query = "SELECT user_id, first_name, last_name, email, birth_date FROM users WHERE user_id = %s;"

        results = query_db(query, query_params=(id,))

        return render_template("edit_users.j2", results=results)
    
    
    if request.method == "POST":
        if request.form.get("edit_users"):

            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            birth_date = request.form["birth_date"]

            try:
                
                # Query to update user
                query = "UPDATE users SET first_name = %s, last_name = %s, email = %s, birth_date = %s WHERE user_id = %s;"
                query_db(query=query, query_params=(first_name, last_name, email, birth_date, id))

                return redirect("/users")
            
            except:

                # Return error if editing in an email that already exists
                return render_template("/users_error.j2")

