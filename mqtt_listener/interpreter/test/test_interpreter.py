import unittest
import unittest.mock as mock
from unittest.mock import patch

from .. import interpreter
from . import *
from .TEST_CONFIG import config
from .TEST_CREDENTIALS import credentials

"""
test_interpreter.py
Tests to ensure that we can write to the database as required
"""


class TestInterpreter(unittest.TestCase):
    """
    Tests for the Interpreter functions.
    """

    def setUp(self):
        """
        Build a toy interpreter class.
        :return:
        """
        self.interpreter = interpreter.Interpreter(config=config, credentials=credentials)

    def test_bad_message_calls_bad_endpoint(self):
        """
        If we pass a bad message, it needs to end up at the bad end-point.
        """
        self.interpreter.bad_message_endpoint = unittest.mock.MagicMock()
        mock_endpoint = self.interpreter.bad_message_endpoint

        bad_messages = (TEST_MESSAGE_IRRELEVANT, TEST_MESSAGE_MISSING_COLUMNS) 
        for bad_message in bad_messages:
            self.interpreter.interpret_message(bad_message)

        self.assertEqual(
            True,
            mock_endpoint.call_count == len(bad_messages),
                "Expected bad message endpoint to be called {0} times; was only called {1} times.".format(
                len(bad_messages),
                mock_endpoint.call_count
            )
        )

    def test_good_message_calls_good_endpoint(self):
        """
        If we pass a good message, it should end up at the good end-point.
        """
        self.interpreter.good_message_endpoint = unittest.mock.MagicMock()
        mock_endpoint = self.interpreter.good_message_endpoint

        good_messages = (TEST_MESSAGE,)
        for good_message in good_messages:
            self.interpreter.interpret_message(good_message)

        self.assertEqual(
            True,
            mock_endpoint.call_count == len(good_messages),
            "Expected good message endpoint to be called {0} times; was only called {1} times.".format(
                len(good_messages),
                mock_endpoint.call_count
            )
        )

    def test_json_to_dict(self):
        """
        Ensure we can convert message to a JSON.
        """
        output = interpreter.message_to_json(TEST_MESSAGE)
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
        sql_statement = interpreter.json_to_statement(TEST_TABLE, TEST_COLUMNS)
        self.assertEqual(
            True,
            TEST_INSERT_STATEMENT == sql_statement,
            "Output SQL statement:\n{0}\nWas not the same as expected statement:\n{1}".format(
                sql_statement, TEST_INSERT_STATEMENT
            )
        )

    def test_invalid_messages_are_rejected(self):
        """
        When we pass in bad messages, ensure that they are rejected.
        """
        for bad_message in (TEST_MESSAGE_IRRELEVANT, ):
            is_message_valid = self.interpreter.validate_message(bad_message)
            self.assertEqual(
                True,
                is_message_valid["valid"] == False,
                "Expected validation for message:\n{0}\nto be False. Got:\n{1}".format(
                    bad_message,
                    is_message_valid["valid"]
                )
            )

    def test_message_with_missing_columns_are_rejected(self):
        """
        When a message is missing some columns, ensure they are rejected.
        """
        for bad_message in (TEST_MESSAGE_MISSING_COLUMNS, ):
            is_message_valid = self.interpreter.validate_message(bad_message)
            self.assertEqual(
                True,
                is_message_valid["valid"] == False,
                "Expected validation for message:\n{0}\nto be False. Got:\n{1}".format(
                    bad_message,
                    is_message_valid["valid"]
                )
            )