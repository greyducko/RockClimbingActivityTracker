-- Group 8 Charles Loughin, Harvey Ng
-- This DDL file is part of the CS340 Portfolio Project deliverables
-- DDL file contains queries to create 5 tables (gyms, users, sessions, attempts, users_gyms) and then insert sample data into the tables
-- Tables are first created, followed by the addition of data into the tables
-- This file was created from a database export; additional comments are added


SET FOREIGN_KEY_CHECKS = 0;
SET AUTOCOMMIT = 0;

-- Create gyms table
CREATE OR REPLACE TABLE gyms (
  gym_id INT AUTO_INCREMENT,
  gym_name VARCHAR(45) NOT NULL,
  PRIMARY KEY (gym_id)
);

-- Create users table
CREATE OR REPLACE TABLE users (
  user_id INT AUTO_INCREMENT,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  email VARCHAR(45) NOT NULL,
  birth_date DATE NULL,
  PRIMARY KEY (user_id),
  CONSTRAINT unique_email UNIQUE(email)
);

-- Create sessions table
CREATE OR REPLACE TABLE sessions (
  session_id INT AUTO_INCREMENT,
  date DATE NOT NULL,
  user_id INT NOT NULL,
  gym_id INT,
  PRIMARY KEY (session_id),
  INDEX fk_sessions_users1_idx (user_id ASC) VISIBLE,
  INDEX fk_sessions_gyms1_idx (gym_id ASC) VISIBLE,
  CONSTRAINT fk_sessions_users1
    FOREIGN KEY (user_id)
    REFERENCES users (user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_sessions_gyms1
    FOREIGN KEY (gym_id)
    REFERENCES gyms (gym_id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

-- Create attempts table
CREATE OR REPLACE TABLE attempts (
  attempt_id INT AUTO_INCREMENT,
  grade INT NOT NULL,
  is_success TINYINT NOT NULL,
  session_id INT NOT NULL,
  PRIMARY KEY (attempt_id),
  UNIQUE INDEX attempt_id_UNIQUE (attempt_id ASC) VISIBLE,
  INDEX fk_attempts_sessions1_idx (session_id ASC) VISIBLE,
  CONSTRAINT fk_attempts_sessions1
    FOREIGN KEY (session_id)
    REFERENCES sessions (session_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Create users_gyms intersection table
CREATE OR REPLACE TABLE users_gyms (
  user_gym_id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  gym_id INT NOT NULL,
  PRIMARY KEY (user_gym_id),
  INDEX fk_users_has_gyms_gyms1_idx (gym_id ASC) VISIBLE,
  INDEX fk_users_has_gyms_users_idx (user_id ASC) VISIBLE,
  CONSTRAINT fk_users_has_gyms_users
    FOREIGN KEY (user_id)
    REFERENCES users (user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_users_has_gyms_gyms1
    FOREIGN KEY (gym_id)
    REFERENCES gyms (gym_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT unique_relationship UNIQUE (user_id, gym_id)
);

-- Begin inserting sample data

-- Insert sample data into users table
INSERT INTO users (first_name, last_name, email, birth_date) 
VALUES
    ('John', 'Doe', 'john.doe@example.com', '1990-05-15'),
    ('Jane', 'Smith', 'jane.smith@example.com', '1985-08-22'),
    ('Michael', 'Johnson', 'michael.johnson@example.com', '1978-11-10'),
    ('Emily', 'Brown', 'emily.brown@example.com', '1993-02-28'),
    ('David', 'Wilson', 'david.wilson@example.com', NULL);

-- Insert sample data into gyms table
INSERT INTO gyms (gym_id, gym_name) 
VALUES
    (1, 'Gym A'),
    (2, 'Gym B'),
    (3, 'Gym C'),
    (4, 'Gym D'),
    (5, 'Gym Z');

-- Insert sample data into sessions table
INSERT INTO sessions (date, user_id, gym_id) 
VALUES
    ('2024-01-01', 1, 1),
    ('2024-01-01', 1, 2),
    ('2024-01-02', 2, 2),
    ('2024-01-03', 3, 3),
    ('2024-01-04', 4, NULL),
    ('2024-02-02', 5, NULL);

-- Insert sample data into attempts table 
INSERT INTO attempts (grade, is_success, session_id) 
VALUES
    (1, 1, 1),
    (3, 1, 1),
    (2, 1, 2),
    (3, 0, 2), 
    (3, 0, 3),
    (7, 1, 4),
    (5, 0, 4),
    (2, 1, 5),
    (3, 1, 5);

-- Insert sample data into users_gyms table
INSERT INTO users_gyms (user_id, gym_id) 
VALUES
    (1, 1),
    (1, 2),
    (2, 2),
    (3, 3),
    (4, 3),
    (4, 4);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;