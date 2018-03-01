import json
import logging
import MySQLdb

logger = logging.getLogger(__name__)

from mqtt_listener.interpreter import config as config, credentials as credentials

"""
Interpreter.py
Python module to convert MQTT messages into their desired endpoints.
Initially will send them to a database.
"""

"""
When a message is received, it should be first validated to make sure:
* it is a JSON file
* It has the required entries to be submitted to a database.

If it is not valid it should be dumped into a suitable end-point (e.g. logged and ignored).

If a message is validated, it is to be submitted to a database.
"""


def interpret_message(message):
    """
    Entrypoint for a message.
    """
    message_valid = validate_message(message)
    if message_valid["valid"]:
        good_message_endpoint(message)
    else:
        bad_message_endpoint(message)


def validate_message(message):
    """
    Is a message valid according to the following criteria:
    * Can be converted into a JSON file
    * Can be inserted into the database structure that we desire
    """
    # Did we get a json message?
    try:
        json_message = message_to_json(message)
    except json.JSONDecodeError as e:
        return {"valid": False, "reason": e}
    except Exception as e:
        return {"valid": False, "reason": e}

    # Do we have all the required columns to pass to the database?
    missing_columns = []
    for column in config.COLUMNS:
        if column not in json_message.keys():
            missing_columns.append(column)
    if len(missing_columns) > 0:
        return {"valid": False, "reason": "Missing column(s): {0}".format(missing_columns)}

    # Everything is good!
    return {"valid": True, "reason": "Pass"}
        

def message_to_json(message):
    """
    When a message is received, convert it into JSON.
    """
    json_message = json.loads(message)
    return json_message


def good_message_endpoint(good_message):
    """
    End point for a validated message.
    """
    pass


def bad_message_endpoint(bad_message, reason=None):
    """
    End point for a message that is invalid in some way.
    """
    pass


def message_to_db(json_message, host=config.DATABASE_SERVER, port=config.DATABASE_PORT, user=credentials.USERNAME,
                  passwd=credentials.PASSWORD, db=config.DATABASE_NAME):
    """
    Take a JSON message and write it to a mysql database.
    :param message: JSON message to be written to database.
    :return: Boolean indicating success
    """
    # Connect to the database
    conn = MySQLdb.connect(
        host=host,
        port=port,
        user=user,
        passwd=passwd,
        db=db
    )
    cursor = conn.cursor()

    # Form the SQL statement
    sql = json_to_statement(config.DATABASE_NAME, config.COLUMNS)

    # Insert into the database
    cursor.execute(sql, json_message)
    conn.commit()

    # Complete
    conn.close()


def json_to_statement(table, columns):
    """
    Convert a JSON message to an INSERT statement.
    """
    statement = "INSERT INTO " + table + " ("
    for i in range(len(columns)):
        statement += columns[i]
        if i < len(columns) - 1:
            statement += ", "
    statement += ") VALUES ("
    for i in range(len(columns)):
        statement += "%(" + columns[i] + ")s"
        if i < len(columns) - 1:
            statement += ", "
    statement += ")"
    return statement