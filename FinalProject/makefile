install:
    pip install -r requirements.txt

lint:
    pylint src/*.py

test:
    pytest test/

build-api:
    docker-compose build flask-api

build-worker:
    docker-compose build worker

run-api:
    docker-compose up flask-api

run-worker:
    docker-compose up worker

stop:
    docker-compose down
