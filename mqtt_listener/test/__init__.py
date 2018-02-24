TEST_MESSAGE = '{"Sensor": "Kitchen", "Measure": "Temperature", "Unit": "deg C", "Time": "13:37:00 01/01/2018", "Value": 25.0, "Debug": 1}'
TEST_JSON = {
        "Sensor":   "Kitchen",
        "Measure":  "Temperature",
        "Unit":     "deg C",
        "Time":     "13:37:00 01/01/2018",
        "Value":    25.0, 
        "Debug":    1
    }
TEST_TABLE = "data"
TEST_COLUMNS = [
    "Sensor",
    "Measure",
    "Unit",
    "Time",
    "Value",
    "Debug",
]
TEST_INSERT_STATEMENT = "INSERT INTO data " \
                        "(Sensor, Measure, Unit, Time, Value, Debug) " \
                        "VALUES (%(Sensor)s, %(Measure)s, %(Unit)s, %(Time)s, %(Value)s, %(Debug)s)"