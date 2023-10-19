-- script that creates the table unique_id on your MySQL.
CREATE TABLE IF NOT EXISTS unique_id(
id INT default 1  unique,
name VARCHAR(256)
);
