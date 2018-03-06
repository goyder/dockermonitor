"""
integration_test_interpreter.py
Larger scale tests that can only be run with other modules running.
"""

from .. import interpreter
import unittest
from . import *
from .TEST_CONFIG import config
from .TEST_CREDENTIALS import credentials


class TestDatabaseIntegration(unittest.TestCase):
    """
    Integration tests for the MySQL database.
    """

    def setUp(self):
        self.interpreter = interpreter.Interpreter(config=config, credentials=credentials)

    def test_submit_message(self):
        """
        Submit a message through the interpreter class.
        :return:
        """
        self.interpreter.message_to_db(TEST_JSON)

    def test_interpreter_message(self):
        """
        Submit a message through the whole process of the interpreter class.
        :return:
        """
        self.interpreter.interpret_message(TEST_MESSAGE)