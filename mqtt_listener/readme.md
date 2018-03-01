# mqtt_listener
---

## Purpose
The purpose of this container is to, as the name suggests, listen to the MQTT host. When it hears a relevant message - one containing data it can use - it will write the data to a database.

## Input Format
The message is to be sent over the MQTT platform as a JSON message, containing the following parameters:
* *Sensor*:     The name of the sensor sending the data.
* *Measure*:    The type of data being sent (e.g. humidity, temperature).
* *Unit*:       Unit of the data.
* *Time*:       What time the sensor sent the data.
* *Value*:      The value of the datum.
* *Debug*:      Whether this is a real data point or simply for debugging purposes.

An input message might therefore be:
`{"Sensor":"Kitchen", "Measure":"Temperature", "Unit":"deg C", "Time":"23-01-2018 20:47:40", "Value":22.70, "Debug":0}`

### Time
Time is presented in the format `%Y-%m-%d %H:%M:%S`.

## Database
In this instance of the monitor, interpreter will:
* Ensure that the data being received is valid (i.e. has all necessary information, has not been mangled, etc)
* Write the data to a MYSQL container.