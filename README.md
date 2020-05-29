<h1>Angular-Flask-Postgres-Nginx-Docker-Demo v1.0</h1>
<h3>Simple Angular-Flask-PostgreSQL seed project with Docker.</h3>

This is a simple Angular-Flask web application skeleton project with following key features:

* The project structure supports multiple development environments with the usage of .env variable and docker.compose.yml files.
* Service Class that encapsulates common SQLAlchemy operations to interact with data model by exposing APIs.
* Support Flask code Testing out of the box. For commands to test, see below.
* Complete PostgreSQL database support with sample db, model and dummy data examples included in the project.
* Reverse proxy using nginx.
* RedisQueue with Celery for asynchronous process 

It is built with following components:
* Angular (v9) - Frontend framework.
* Flask(1.1.2) - Micro web framework (Python-3.6.2) for the backend.
* PostgreSQL - Database support.
* Flask-SQLAlchemy - Flask based ORM wrapper on SQLAlchemy.
* nginx - web server (It's also used for reverse proxy). External user hits the nginx which distributes the request between Frontend and Backend using url.
* uwsgi - It's a WSGI server that help running web application written in Python. It comes with direct support for popular NGINX web server.
* Docker - Usage of Docker Compose to build and host the application.

<h3>Project Components (Directory Structure)</h3>
**client**
<p>This directory holds the Angular code.</p>

**nginx**
<p>This directory holds the nginx config file and Dockerfile for running the nginx container. This container serves the Angular code and also passes request to backend.</p>

**postgresql**
<p>This directory holds the Dockerfile for running PostgreSQL database. It also contains init.sql script to create a sample database when postres docker container initializes.</p>

**server**
<p>This directory contains the server side code. It hosts the Flask app, tests setup and other configs and settings files required by the backend. It also has Dockerfile for running the flask container. This container hosts the backend code.</p>

**Environment variable**
<p>A simple .env file to set the environment variables for Flask and Postgres. We can have multiple versions of this file for different environments.</p>

**docker-compose.yml**
<p>This file is used by the Docker to create the containers and run your app. We can have multiple versions of this file for different environments.</p>

<h3>Architecture</h3>
For this seed project, I am using 3 Docker containers:

* NGINX - Web Server
* FLASK - Flask web application with uwsgi server.
* PostgreSQL - Database.
<p>The three components are all created from Docker images that expand on the respective official images from Docker Hub. Each of these images are built using separate Dockerfiles. Docker Compose is then used to create all three containers and connect them correctly into a unified application.</p>

**Working**
<p>The request from an external user hits the nginx web server on port 80. Depending on the URL,the request is served using Angular code or it is sent to Flask web application. In this app, all request URL starting with /api is sent to Flask web service. The Flask docker container is also running and it exposes port 5000. These setting are defined in nginx.conf file. In this way, nginx is aware of both Frontend and Backend services. The Flask container talks to the PostgreSQL database on port 5432 for any request that require database operations.</p>

## Usage

**NOTE**: Make sure you have Docker, node, npm and angular-cli installed. Check Angular
Prerequisites [here](https://github.com/angular/angular-cli#prerequisites).

- Clone this repository
- **Not Required** - Navigate to client directory and execute `ng build --prod` to create production build for Angular.
- Then navigate back and execute following commands:
  - `docker-compose build`
  - `docker-compose up`
  - _OR_ just run one command: `docker-compose -f docker-compose.yml up --build`
- Open Browser and type following URL:
- `localhost` - It should display the Welcome message from Angular and a default message from
  backend.
- `localhost/api` - It should display welcome message from Flask.
- `localhost/api/ping` - To get a `json` from Flask.
- `http://localhost/api/users` - Fetches all users from `users` table.

This seed project is good for starting up with any Angular-Flask-Docker project, so check it out and feel free to fork, update, plug in your project etc. Let me know if you find any issues.

## Working with PostgreSQL

- Check to see if `postgres` is running on port `5432`:
  - Run: `nc -zv localhost 5432`
  - Correct Output: `Connection to localhost port 5432 [tcp/postgresql] succeeded!`
  - If you see above output, everything is good
- To log into the container running Postgres:
  - check docker running processes: `docker ps -a`
  - Find out the **container_id** of the Postgres database and run: `docker exec -it <container_id> bash`
  - You should now be in postgres docker container terminal:
  - Open PostgreSQL command line by running `psql -U <database_username>`.
    - For this project, run: `psql -U postgres`
  ```
    root@0dffa1473a46:/# psql -U postgres
    psql (9.6.9)
    Type "help" for help.
    postgres=#
  ```
  - `\l` - show all databases
  - `\c users_dev` - connect to `users_dev` database.
  - `\dt` - shows list of tables in the selected database
  - check data: `SELECT * FROM users;`

## Running Python Tests:

- All Flask/Python unit tests resides inside the `server/tests` directory and managed by `manage .py` Python file.
- Run the sample tests using following command:
  - `docker-compose -f docker-compose.yml run --rm backend python manage.py test`


To use make file: make and then any command in make file. Eg.
make backend-access