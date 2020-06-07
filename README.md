<h1>Angular-Flask-Postgres-Docker-Nginx-Celery-Skeleton v1.0</h1>
<h3>Simple Angular-Flask-PostgreSQL with Docker, nginx and celery skeleton project.</h3>

This skeleton project is good for starting up with any Angular-Flask-Docker project, so check it out and feel free to fork, update, plug in your project etc. Let me know if you find any issues at saurabh.prasad197@gmail.com.
It includes but is not limited to the following -
* Complete PostgreSQL database support with sample db, model and dummy data examples included in the project.
* Reverse proxy using nginx.
* RedisQueue with Celery for asynchronous process 

<p>All components created from Docker images that expand on the respective official images from Docker Hub. Docker-compose file binds them together </p>
## Working
<p>The request from an external user hits the nginx web server on port 8080. Depending on the URL,the request is served using Angular code or it is sent to Flask web application. In this app, all request URL starting with /api is sent to Flask web service. The Flask docker container is also running and it exposes port 5000. These setting are defined in nginx.conf file. In this way, nginx is aware of both Frontend and Backend services. The Flask container talks to the PostgreSQL database on port 5432 for any request that require database operations. A separate celery worker is created with takes care of processing any long process asynchronously. Its activated on clicking 'Add dummy' button on frontend</p>

**NOTE**: Make sure you have Docker, node, npm and angular-cli installed. Check Angular
Prerequisites [here](https://github.com/angular/angular-cli#prerequisites).

## How to run
- Clone this repository
There are two branches- master and frontend_backend_db_docker. use -> git checkout branch_name
- Then navigate to project_dir and execute following commands:
  - `docker-compose build`
  - `docker-compose up`
  - _OR_ just run one command: `docker-compose -f docker-compose.yml up --build`
 
- Open Browser and type following URL:
    - `localhost:8080` - frontend landing page using nginx 
    - `localhost:4200` - frontend app
    - `localhost:5000/api/health` - Health check from backend
    - `http://localhost:5000/api/blogs` - Fetches all blogs from `blogs` table in `blogs_db` database.


- To close the application
    - Ctrl + C or docker-compose down (optional)

## To run things locally
- frontend : cd frontend/ -> npm install -> ng serve
- backend : cd backend/ -> pip install -r requirements.txt -> export FLASK_APP=backend/run.py -> flask run
- celery : cd backend/ -> celery -A app.celery.celery_worker.celery worker --loglevel=info
- postgres and redis: docker-compose -f docker-compose-local.py build -> docker-compose -f docker-compose-local.py up

## Additional Notes:
-   NGINX routes '/' to frontend and '/api/' to backend
-   The project structure supports multiple environments defined in setting.py
-   Edit environment variables in .env and .env_docker
-   ENV variables are loaded through setting.py
-   Some helpful commands are provided in Makefile
     - Eg. make backend-access
- docker-compose-local.yml has just postgresql and redis
- postgres has health check that ensures backend is deployed once postgres is up
- I have written some tests for backend using pytest and jasmine/karma for frontend
- run tests using python tests/tests.py and ng test respectively
 
