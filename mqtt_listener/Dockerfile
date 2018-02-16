FROM python:3.6-alpine
RUN pip install paho-mqtt
ADD mqtt_listener_entrypoint.py /
CMD [ "python", "./mqtt_listener_entrypoint.py" ] 
