<h1>Angular-Flask-Postgres-Docker-Demo v1.0</h1>
<h3>Simple Angular-Flask-PostgreSQL seed project with Docker.</h3>

## Usage

**NOTE**: Make sure you have Docker, node, npm and angular-cli installed. Check Angular
Prerequisites [here](https://github.com/angular/angular-cli#prerequisites).

- Clone this repository
- Then navigate to project_dir and execute following commands:
  - `docker-compose build`
  - `docker-compose up`
  - _OR_ just run one command: `docker-compose -f docker-compose.yml up --build`
  
- Open Browser and type following URL:
- `localhost:4200` - frontend app
- `localhost/api/health` - Health check from backend
- `http://localhost/api/blogs` - Fetches all blogs from `blogs` table in `blogs_db` database.

This seed project is good for starting up with any Angular-Flask-Docker project, so check it out and feel free to fork, update, plug in your project etc. Let me know if you find any issues at saurabh.prasad197@gmail.com.

## To run things individually
- frontend : npm install followed by ng serve
- backend : pip install requirements.txt followed by running the flask app
- postgres : comment frontend and backend part in docker-compose.yml and run as standard docker-compose project to deploy only database which will be automatically connected by local backend
