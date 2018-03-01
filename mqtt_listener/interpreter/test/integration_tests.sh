#!/bin/bash
docker-compose exec mqtt_listener python -m unittest /test/test_integration_interpreter.py
