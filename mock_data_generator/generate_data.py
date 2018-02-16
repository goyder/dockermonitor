import paho.mqtt.client as mqtt
import time

print("Hello, world!")

client = mqtt.Client()
client.connect("mosquitto", port=1883)
while True:
    client.publish("home/garden/pond", payload="Hello, pond!")
    time.sleep(1)
