-- Create a limited user for accessing the MySQL database from Grafana.
CREATE USER IF NOT EXISTS 'grafana' IDENTIFIED BY 'grafana';
GRANT SELECT ON main_db.data TO 'grafana';
