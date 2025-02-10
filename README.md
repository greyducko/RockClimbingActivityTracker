# Rock Climbing Activity Tracker

A CRUD application developed for Oregon State University's CS340 Databases class by Harvey Ng and Charles Loughin.

Serves as a mock database administrator portal to demonstrate CRUD functionality for an application that allows users to track their rock climbing training sessions.

The project makes use of or adapts some portions of the code base from outside sources, cited below:

HTML and Jinja templates (attempts.j2, edit_gyms.j2, edit_users_gyms.j2, edit_users.j2, gyms.j2, index.j2, users_gyms.j2, users.j2) were adapted from the scaffolding provided by the flask-starter-app provided in the course materials: https://github.com/osu-cs340-ecampus/flask-starter-app/

The database connector (db_connector.py) and credentials file (db_connector.py) were also adapted from the scaffolding provided by the flask-starter-app provided in the course materials, and remain largely unchanged from their source: https://github.com/osu-cs340-ecampus/flask-starter-app/

The Flask app (app.py, attempts.py, gyms.py, sessions.py, users_gyms.py, users.py) was built using the scaffolding provided by the flask-starter-app (https://github.com/osu-cs340-ecampus/flask-starter-app/), and adapted to make use of Flask blueprints based on the following source: https://realpython.com/flask-blueprint/

Sources Cited:
flask-starter-app: https://github.com/osu-cs340-ecampus/flask-starter-app/
Authors: Michael Curry, Andrew Kamand, @mlapresta (on github)

Use a Flask Blueprint to Architect Your Applications: https://realpython.com/flask-blueprint/
Author: Miguel Garcia
