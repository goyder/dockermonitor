FROM python:3.6-alpine
RUN pip install paho-mqtt
ADD entrypoint.py /
CMD [ "python", "./entrypoint.py" ] 
