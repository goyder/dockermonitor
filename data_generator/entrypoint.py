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

# Connect to our MQTT server
client = mqtt.Client()
client.connect("mosquitto", port=1883)

# We'll mock up some values and have them wander by random force.
temperature = 25.0
humidity    = 70
t = 0

while True:
    message = '{{"Sensor":"Kitchen","Measure":"Temperature","Unit":"deg C", "Time":"{time}","Value":"{value}","Debug":1}}'.format(
        time=time.strftime("%H:%M:%S %d/%m/%Y"),
        value=temperature
    )
    client.publish("home/kitchen", payload=message)

    message = '{{"Sensor":"Kitchen","Measure":"Humidity","Unit":"percent", "Time":"{time}","Value":"{value}","Debug":1}}'.format(
        time=time.strftime("%H:%M:%S %d/%m/%Y"),
        value=humidity
    )
    client.publish("home/kitchen", payload=message)

    # Alter the weather conditions
    temperature += random.random()*0.05
    humdity = humidity + math.sin(t/10)*20 
    
    # Tick
    t += 1
    time.sleep(1)