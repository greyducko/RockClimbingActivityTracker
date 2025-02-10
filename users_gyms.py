# Group 8 Charles Loughin, Harvey Ng
# This module adapted from starter code: https://github.com/osu-cs340-ecampus/flask-starter-app/ (Authors: Michael Curry, Andrew Kamand, @mlapresta (on github)) (
# Code adapted: function to query database; request.method
# Date: 3/18/2024
# Flask blueprint and blueprint.route code adapted from: https://realpython.com/flask-blueprint/
# Original work: SQL queries; form inputs


from flask import Blueprint, request, render_template, redirect
from database.db_connector import query_db
from flask_mysqldb import MySQL

# Create blueprint so routes in this module can be accessed from app.py
users_gyms_blueprint = Blueprint("users_gyms_blueprint", __name__)

# Route handles read and insert for users_gyms 
@users_gyms_blueprint.route("/users_gyms", methods = ["POST", "GET"])
def users_gyms():

    if request.method == "POST":

        if request.form.get("add_users_gyms"):
            try:
                user_id = request.form["user_id"]
                gym_id=request.form["gym_id"]
    
                # Query to insert into users_gyms table
                query = "INSERT INTO users_gyms(user_id, gym_id) VALUE (%s,%s);"
                query_db(query, query_params=(user_id, gym_id))

                return redirect("/users_gyms")
            except:

                # Return error if the relationship already exists
                return render_template("/users_gyms_error.j2")
    
    
    if request.method == "GET":

        # Query to read user_gyms table
        query = "SELECT user_gym_id, users.first_name AS first_name, users.last_name As last_name, gyms.gym_name AS gym_name FROM users_gyms INNER JOIN users ON users.user_id = users_gyms.user_id INNER JOIN gyms ON gyms.gym_id = users_gyms.gym_id;"
        
        results = query_db(query)


        # Query to read gym names to populate dropdown when inserting into users_gyms table
        query2 = "SELECT gym_id, gym_name FROM gyms"
        gym_names = query_db(query2)

        # Query to get drop down of users when inserting into users_gyms table
        query3 = "SELECT user_id, CONCAT(first_name, ' ',last_name) AS full_name FROM users;"
        full_names=query_db(query=query3)

        return render_template("users_gyms.j2", users_gyms=results, gym_names = gym_names, full_names=full_names)

# Route handles delete for users_gyms 
@users_gyms_blueprint.route("/delete_users_gyms/<int:id>")
def delete_users_gyms(id):

    # Query to delete the row with our passed id
    query = "DELETE FROM users_gyms WHERE user_gym_id = '%s';"
    query_db(query=query, query_params=(id,))
    
    return redirect("/users_gyms")

# Route handles edit for users_gyms 
@users_gyms_blueprint.route("/edit_users_gyms/<int:id>", methods=["POST", "GET"])
def edit_users_gyms(id):

    if request.method == "GET":

        # Query to prepopulate edit table showing row to be edited
        query = "SELECT user_gym_id, CONCAT(users.first_name,' ', users.last_name) AS 'first_name, last_name', gyms.gym_name AS gym_name FROM users_gyms INNER JOIN users ON users.user_id = users_gyms.user_id INNER JOIN gyms ON gyms.gym_id = users_gyms.gym_id WHERE user_gym_id = %s;"

        results = query_db(query=query, query_params=(id,))
        

        # Query to prepopulate full_name when editing users_gyms table 
        query2 = "SELECT users.user_id, CONCAT(first_name, ' ',last_name) AS full_name FROM users INNER JOIN users_gyms ON users.user_id = users_gyms.user_id WHERE users_gyms.user_gym_id = %s;"
        full_name=query_db(query=query2, query_params=(id,))

        # Query to get dropdown of gym names when editing users_gyms table
        query3 = "SELECT gym_id, gym_name FROM gyms"
        gym_names = query_db(query=query3)
    
        return render_template("edit_users_gyms.j2", results=results, gym_names=gym_names, full_name=full_name)
    
    if request.method == "POST":

        if request.form.get("edit_users_gyms"):
            try:
                gym_id = request.form["gym_id"]

                # Query to update users_gyms table by changing the gym_id
                query = "UPDATE users_gyms SET users_gyms.gym_id = %s WHERE users_gyms.user_gym_id = %s;"
                query_db(query=query, query_params=(gym_id, id))

                return redirect("/users_gyms")
            
            except:

                # Return error if trying to submit an existing relationship
                return render_template("/users_gyms_error.j2")
        


