-- Create the Database
CREATE DATABASE HealthIndicator;

-- Switch to the Database
USE HealthIndicator;

-- Create the Table
CREATE TABLE health_indicatorr (
    id INT AUTO_INCREMENT PRIMARY KEY,
    week_number INT,
    current_date_now DATETIME,
    overall_score FLOAT,
    push_up FLOAT,
    pull_up FLOAT,
    squat FLOAT,
    fivekm_time FLOAT,
    crunches FLOAT,
    push_up_norm FLOAT,
    pull_up_norm FLOAT,
    squat_norm FLOAT,
    fivekm_time_norm FLOAT,
    crunches_norm FLOAT,
);


