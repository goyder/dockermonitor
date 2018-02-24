import json

"""
Interpreter.py
Python module to convert MQTT messages into their desired endpoints.
Initially will send them to a database.
"""

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
