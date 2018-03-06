# mqtt_listener_entrypoint.py
# Set up an MQTT client that listens for relevant environmental pushes.
# When it hears something it cares about, publish to the database.

import paho.mqtt.client as mqtt
import yaml
import logging.config
import logging

import CONFIG
import CREDENTIALS
import interpreter.interpreter as interpreter

with open("logging.yaml", 'r') as f:
    logging_config = yaml.safe_load(f.read())
logging.config.dictConfig(logging_config)
logging.info("I am running.")


def mock_on_message(client, userdata, msg):
    logging.info(msg.topic + ": " + str(msg.payload))


def on_connect(client, userdata, flags, rc):
    logging.info("Connected with result code: " + str(rc))
    client.subscribe("home/#")


def on_message(client, userdata, msg):
    """
    Validate and write the message.
    :param client:
    :param userdata:
    :param msg:
    :return:
    """
    payload = str(msg.payload, encoding="utf-8")
    logging.info("Message received:\n{0}".format(payload))
    interpreter_instance.interpret_message(payload)


# Take it away
client = mqtt.Client()
interpreter_instance = interpreter.Interpreter(config=CONFIG.config, credentials=CREDENTIALS.credentials)
client.on_connect = on_connect
client.on_message = on_message
client.connect("mosquitto", port=1883)
client.loop_forever()
