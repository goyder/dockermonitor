import logging
logger = logging.getLogger(__name__)

import json
try:
    import MySQLdb
except ModuleNotFoundError:
    logger.info("Could not import MySQL module. Are you running outside of Docker? Expect dramas.")


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


class Interpreter:
    """
    Object to handle a message to its proper endpoint.
    """

    def __init__(self, config, credentials):
        """
        Validate we have all the config data we need.
        :param config:
        """
        # Check if anything is missing
        missing_config = []
        for config_name in [
            "DATABASE_SERVER",
            "DATABASE_PORT",
            "DATABASE_NAME",
            "TABLE_NAME",
            "COLUMNS",
        ]:
            if config_name not in config.keys():
                missing_config.append(config_name)

        missing_credentials = []
        for credentials_names in [
            "USERNAME",
            "PASSWORD",
        ]:
            if credentials_names not in credentials.keys():
                missing_credentials.append(credentials_names)

        # Did we pass?
        if len(missing_config) > 0 or len(missing_credentials) > 0:
            raise ValueError("Interpreter was missing following config and credential values to start:{0}".format(
                "\n".join(missing_config + missing_credentials)
            ))

        self.config = config
        self.credentials = credentials

    def interpret_message(self, message):
        """
        Entrypoint for a message.
        """
        message_valid = self.validate_message(message)
        if message_valid["valid"]:
            self.good_message_endpoint(message_valid["json_message"])
        else:
            self.bad_message_endpoint(message, reason=message_valid["reason"])

    def validate_message(self, message):
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
        for column in self.config["COLUMNS"]:
            if column not in json_message.keys():
                missing_columns.append(column)
        if len(missing_columns) > 0:
            return {"valid": False, "reason": "Missing column(s): {0}".format(missing_columns)}

        # Everything is good!
        return {"valid": True, "reason": "Pass", "json_message": json_message}

    def good_message_endpoint(self, good_message):
        """
        End point for a validated message.
        """
        logger.info("Good message, sending to database. Message:\n{0}".format(good_message))
        self.message_to_db(good_message)

    def bad_message_endpoint(self, bad_message, reason=None):
        """
        End point for a message that is invalid in some way.
        """
        logger.info("Invalid message:\n{0}\nReason:\n{1}".format(bad_message, reason))

    def message_to_db(self, json_message):
        """
        Take a JSON message and write it to a mysql database.
        :param message: JSON message to be written to database.
        :return: Boolean indicating success
        """
        conn = MySQLdb.connect(
            host=self.config["DATABASE_SERVER"],
            user=self.credentials["USERNAME"],
            password=self.credentials["PASSWORD"],
            database=self.config["DATABASE_NAME"]
        )
        cursor = conn.cursor()

        # Form the SQL statement
        sql = json_to_statement(self.config["TABLE_NAME"], self.config["COLUMNS"])

        # Insert into the database
        cursor.execute(sql, json_message)
        conn.commit()

        # Complete
        conn.close()


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
