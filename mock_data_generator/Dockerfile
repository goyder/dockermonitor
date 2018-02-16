FROM python:3.6-alpine
RUN pip install paho-mqtt
ADD generate_data.py /
CMD [ "python", "./generate_data.py" ] 
