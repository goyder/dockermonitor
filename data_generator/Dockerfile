FROM python:3.6-alpine
RUN pip install paho-mqtt
ADD . /
CMD [ "python", "./entrypoint.py" ] 
