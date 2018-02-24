import unittest
import unittest.mock as mock

import mqtt_listener.interpreter 
from . import *

"""
test_interpreter.py
Tests to ensure that we can write to the database as required
"""

class TestInterpreter(unittest.TestCase):
    """
    Tests for the Interpreter functions.
    """

    def test_json_to_dict(self):
        """
        Ensure we can convert message to a JSON.
        """
        output = mqtt_listener.interpreter.message_to_json(TEST_MESSAGE)
        self.assertEqual(
            True,
            TEST_JSON == output,
            "Output dict:\n{0}\nWas not the same as expected output dict:\n{1}".format(
                output, TEST_JSON
            )
        )

    def test_query_generation(self):
        """
        Ensure that we generate an INSERT query with the list of columns and data.
        """
        sql_statement = mqtt_listener.interpreter.json_to_statement(TEST_TABLE, TEST_COLUMNS)
        self.assertEqual(
            True,
            TEST_INSERT_STATEMENT == sql_statement,
            "Output SQL statement:\n{0}\nWas not the same as expected statement:\n{1}".format(
                sql_statement, TEST_INSERT_STATEMENT
            )
        )


    
