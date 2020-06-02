backend=$(shell docker-compose ps -q backend)
frontend=$(shell docker-compose ps -q frontend)

# Init
init:
	docker-compose up

# Build
build:
	docker-compose build

# Init the debuger
backend-debug:
	export FLASK_DEBUG=1 && docker-compose -f docker-compose.debug.yaml up

# Access backend
backend-access:
	docker exec -it $(backend) sh

# Access frontend
frontend-access:
	docker exec -it $(frontend) sh

# Install a module
# usage --> make backend-install-module module="MODULE NAME"
backend-install-module:
	docker exec -t $(backend) pipenv install '$(module)'

# Run the tests in the backend
backend-tests:
	docker exec -t $(backend) pipenv run python tests/tests.py

# Run the tests in the frontend
frontend-tests:
	docker exec -it $(frontend) ng test

# Run only one test
# usage --> make backend-one-test test="TEST NAME"
backend-one-test:
	docker exec -t $(backend) pipenv run python tests/tests.py '$(test)'

# Init database
db-init:
	docker exec -t $(backend) pipenv run flask db init

# Generate database migrations
db-migrate:
	docker exec -t $(backend) pipenv run flask db migrate -m '$(comment)'

# Merge two heads
db-merge:
	docker exec -t $(backend) pipenv run alembic -c migrations/alembic.ini merge heads

# Apply database upgrade
db-upgrade:
	docker exec -t $(backend) pipenv run flask db upgrade

# Apply database downgrade
db-downgrade:
	docker exec -t $(backend) pipenv run flask db downgrade

