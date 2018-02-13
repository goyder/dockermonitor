-- Create a limited user for accessing the MySQL database from Grafana.
CREATE USER IF NOT EXISTS 'grafana'@'%' IDENTIFIED BY 'grafana';
DROP USER IF EXISTS ''@'%';
USE main_db;
GRANT SELECT ON main_db.* TO 'grafana'@'%';
FLUSH TABLES mysql.user;
