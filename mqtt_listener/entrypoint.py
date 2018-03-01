# mqtt_listener_entrypoint.py
# Set up an MQTT client that listens for relevant environmental pushes.
# When it hears something it cares about, publish to the database.

import paho.mqtt.client as mqtt
import yaml
import logging.config
import logging
import os

import interpreter

with open("logging.yaml", 'r') as f:
    config = yaml.safe_load(f.read())
logging.config.dictConfig(config)

logging.info("I am running.")

# Stub, to prove this works
def mock_on_message(client, userdata, msg):
    print(msg.topic + ": " + str(msg.payload))

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    client.subscribe("home/#")

# Take it away
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = mock_on_message
client.connect("mosquitto", port=1883)
client.loop_forever()
