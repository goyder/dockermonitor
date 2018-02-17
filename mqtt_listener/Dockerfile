FROM python:3.6-alpine
RUN apk add --update --no-cache mariadb-client-libs \
  && apk add --no-cache --virtual .build-deps \
  mariadb-dev \ 
  gcc \
  musl-dev \
RUN pip install paho-mqtt mysqlclient
RUN apk del .build-deps
ADD mqtt_listener_entrypoint.py /
CMD [ "python", "./mqtt_listener_entrypoint.py" ] 
