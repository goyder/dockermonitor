TEST_MESSAGE = '{"Sensor": "Kitchen", "Measure": "Temperature", "Unit": "deg C", "Time": "2018-01-01 13:37:00", "Value": 25.0, "Debug": 1}'
TEST_JSON = {
        "Sensor":   "Kitchen",
        "Measure":  "Temperature",
        "Unit":     "deg C",
        "Time":     "2018-01-01 13:37:00",
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

TEST_MESSAGE_IRRELEVANT = "Ever Since I Turned the Lights On"
TEST_MESSAGE_MISSING_COLUMNS = '{"Measure": "Temperature", "Unit": "deg C", "Time": "2018-01-01 13:37:00", "Value": 25.0, "Debug": 1}'
TEST_MESSAGE_EXTRA_COLUMNS = '{"Sensor": "Kitchen", "Measure": "Temperature", "Unit": "deg C", "Time": "2018-01-01 13:37:00", "Value": 25.0, "Debug": 1}'
