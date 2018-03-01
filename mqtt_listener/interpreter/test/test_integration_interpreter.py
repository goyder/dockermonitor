"""
integration_test_interpreter.py
Larger scale tests that can only be run with other modules running.
"""

from mqtt_listener import interpreter
import unittest
from . import *


class TestDatabaseIntegration(unittest.TestCase):
    """
    Integration tests for the MySQL database.
    """

    def test_submit_message(self):
        """
        Submit a message through the interpreter module.
        :return:
        """
        interpreter.message_to_db(TEST_JSON)
