-- Group 8 Charles Loughin, Harvey Ng
-- This DML file is part of the CS340 Portfolio Project deliverables
-- The structure of this file goes table by table, listing the queries used to implement each operation (create, read, update, and/or delete)



-- ------------------------ users table (Create, Read, Update, Delete) -------------------------------


-- CREATE --
-- Query to insert into users table
INSERT INTO users (first_name, last_name, email, birth_date) VALUE (%s, %s,%s,%s);


-- READ -- 
-- Query to read users table
SELECT user_id, first_name, last_name, email, birth_date FROM users;


-- UPDATE -- 
-- Queries involved in updating a user:
-- Query to get first_name, last_name, email, and birth_date of user being edited to prepopulate fields
SELECT user_id, first_name, last_name, email, birth_date FROM users WHERE user_id = %s;

-- Query to update user with form values:
UPDATE users SET first_name = %s, last_name = %s, email = %s, birth_date = %s WHERE user_id = %s;


-- DELETE --
-- Query to delete the selected user from users table
DELETE FROM users WHERE user_id = %s;



-- ------------------------ gyms table (Create, Read, Update) -------------------------------


-- CREATE -- 
-- Query to insert into gyms table
INSERT INTO gyms (gym_name) VALUE (%s);


-- READ -- 
-- Query to read gyms table
SELECT gym_id, gym_name FROM gyms;


-- UPDATE -- 
-- Queries involved in updating a gym:
-- Query to get gym_name to prepopulate field
SELECT gym_id, gym_name FROM gyms WHERE gym_id = %s;

-- Query to update table with form values
UPDATE gyms SET gym_name = %s WHERE gym_id = %s;



-- ------------------------ users_gyms table (Create, Read, Update, Delete) -------------------------------


-- CREATE -- 
-- Queries involved in inserting:
-- Query to insert new user_gym relationship
INSERT INTO users_gyms(user_id, gym_id) VALUE (%s,%s);

-- Query to read gym names to populate dropdown when inserting
SELECT gym_id, gym_name FROM gyms;

-- Query to read user full_names to populate drop down table when inserting
SELECT user_id, CONCAT(first_name, ' ',last_name) AS full_name FROM users;


-- READ -- 
-- Query to display users_gyms table and replaces foreign keys with relevant values
SELECT user_gym_id, users.first_name AS first_name, users.last_name As last_name, gyms.gym_name AS gym_name FROM users_gyms INNER JOIN users ON users.user_id = users_gyms.user_id INNER JOIN gyms ON gyms.gym_id = users_gyms.gym_id;


-- UPDATE -- 
-- Queries involved in editing users_gyms table:
-- Query to read gym names to populate dropdown 
SELECT gym_id, gym_name FROM gyms;

-- Query to populate full_name
SELECT users.user_id, CONCAT(first_name, ' ',last_name) AS full_name FROM users INNER JOIN users_gyms ON users.user_id = users_gyms.user_id WHERE users_gyms.user_gym_id = %s;

-- Query to prepopulate edit table with the values in the row that was selected
SELECT user_gym_id, CONCAT(users.first_name,' ', users.last_name) AS 'first_name, last_name', gyms.gym_name AS gym_name FROM users_gyms INNER JOIN users ON users.user_id = users_gyms.user_id INNER JOIN gyms ON gyms.gym_id = users_gyms.gym_id WHERE user_gym_id = %s;

-- Query to update users_gyms table
UPDATE users_gyms SET users_gyms.gym_id = %s WHERE users_gyms.user_gym_id = %s;


-- DELETE -- 
-- Query to delete selected user_gym relationship
DELETE FROM users_gyms WHERE user_gym_id = '%s';



-- -------------------------- sessions table (Create, Read, Update) -------------------------------


-- CREATE -- 
-- Queries involved in inserting a new session:
-- Query to insert session:
INSERT INTO sessions (date, user_id, gym_id) VALUE (%s, %s,%s);

-- Query to populate dropdown of full_names to choose from
SELECT user_id, CONCAT(first_name, ' ', last_name) AS full_name FROM users;

-- Query to populate dropdown of gym_names to choose from
SELECT gym_id, gym_name FROM gyms;


-- READ -- 
-- Query to read sessions table
SELECT session_id, date, first_name, last_name, gym_name FROM sessions INNER JOIN users ON sessions.user_id = users.user_id LEFT OUTER JOIN gyms ON sessions.gym_id = gyms.gym_id;


-- UPDATE -- 
-- Queries involved in editing session:
-- Query to prepopulate row being edited
SELECT session_id, date, CONCAT(first_name,' ', last_name) AS full_name, gym_name FROM sessions INNER JOIN users ON sessions.user_id = users.user_id LEFT JOIN gyms ON sessions.gym_id = gyms.gym_id WHERE session_id = %s;

-- Query to populate dropdown of gym_names
SELECT gym_id, gym_name FROM gyms;

-- Query to update a session where gym_id is NULL
UPDATE sessions SET gym_id = NULL WHERE session_id = %s;

-- Query to update a session where gym_id is not NULL
UPDATE sessions SET gym_id = %s WHERE session_id = %s;



-- -------------------------- attempts table (Create, Read) -------------------------------


-- CREATE -- 
-- Queries involved in inserting a new attempt:
-- Query to insert a new attempt
INSERT INTO attempts (grade, is_success, session_id) VALUE (%s, %s,%s);

-- Query to get session_id and session_date to populate dropdown 
SELECT sessions.session_id AS session_id, sessions.date AS session_date FROM sessions;


-- READ -- 
-- Query to read attempts table 
SELECT attempt_id, grade, is_success, attempts.session_id, sessions.date AS session_date FROM attempts INNER JOIN sessions ON attempts.session_id = sessions.session_id;

