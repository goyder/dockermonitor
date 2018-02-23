import unittest
import unittest.mock as mock

import mqtt_listener.interpreter 

"""
test_interpreter.py
Tests to ensure that we can write to the database as required
"""

class TestInterpreter(unittest.TestCase):
    """
    Tests for the Interpreter functions.
    """

    def test_initalisation(self):
        """
        Do nothing.
        """
        mqtt_listener.interpreter.validate_payload("What")