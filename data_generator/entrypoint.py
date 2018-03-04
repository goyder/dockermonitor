"""
entrypoint.sh
Entry point for the data_generator container.
This container is to generate mock data for the rest of the system to read and
use if required.
Mostly for debug purposes.
"""
import paho.mqtt.client as mqtt
import math
import random
import time
import json

import config

# Connect to our MQTT server
client = mqtt.Client()
client.connect(config.HOST_URL, port=config.HOST_PORT)

# We'll mock up some values and have them wander by random force.
temperature = 25.0
humidity = 70
t = 0

while True:
    message = {
        "Sensor":   "Kitchen",
        "Measure":  "Temperature",
        "Unit":     "deg C",
        "Time":     time.strftime("%Y-%m-%d %H:%M:%S"),
        "Value":    temperature,
        "Debug":    1
    }
    client.publish("home/kitchen", payload=json.dumps(message))

    message = {
        "Sensor":   "Kitchen",
        "Measure":  "Humidity",
        "Unit":     "percent",
        "Time":     time.strftime("%Y-%m-%d %H:%M:%S"),
        "Value":    humidity,
        "Debug":    1
    }
    client.publish("home/kitchen", payload=json.dumps(message))

    # Alter the weather conditions
    temperature += random.random()*0.05
    humidity = humidity + math.sin(t/10)*0.3
    
    # Tick
    t += 1
    time.sleep(30)

