-- script that creates the table id_not_null on your MySQL
CREATE TABLE IF NOT EXISTS id_not_null(
id INT default 1,
name VARCHAR(256)
);