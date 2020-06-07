backend=$(shell docker-compose ps -q backend)
frontend=$(shell docker-compose ps -q frontend)


# Init
build:
	docker-compose build

build-local:
	docker-compose -f docker-compose-local.yml build

# Run
run:
	docker-compose up
#run-local:
	docker-compose -f docker-compose-local.yml up

# Access backend
backend-access:
	docker exec -it $(backend) sh

# Access frontend
frontend-access:
	docker exec -it $(frontend) sh

# Logs backend
backend-access:
	docker logs backend_container

# Logs frontend
frontend-access:
	docker logs frontend_container

# Init the debugger
backend-debug:
	export FLASK_DEBUG=1 && docker-compose -f docker-compose.debug.yaml up

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

# postgresql login
db-login:
	psql -h localhost -p 5432 -U postgres -W

# Other DB commands-
# exit: \q
# show db: \l
# connect: \c db_name
# show tables: \dt
# delete table tb_name

# Init database (Optional)
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

# Docker IP
docker-ip:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'

docker-process:
	docker ps

# stop all containers:
docker-stop:
	docker kill $(docker ps -q)

# remove all containers
docker-remove:
	docker rm $(docker ps -a -q)

# remove all docker images
docker-remove-images:
	docker rmi $(docker images -q)

# Other docker commands-
# port mapping
# docker run -p 80:8080 mysql
#
# volume mapping
# docker run -v /opt/datadir:/var/lib/mysql mysqql
#
# docker exec -t CONTAINER_ID command to run


# redis
redis-login:
	redis-cli -h localhost -p 6379

# Other redis commands-
# redis-cli -h redis
# set name value
# get name




