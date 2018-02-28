import json

from mqtt_listener import config

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
