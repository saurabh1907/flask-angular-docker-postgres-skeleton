#FROM Ubuntu
#FROM python:alpine3.7
FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /backend

# Update working directory
WORKDIR /backend

# to create a user
#ARG username
#RUN adduser -D ${username}
#RUN chown -R ${username} /app
#USER ${username}

# copy everything from this directory to server/flask docker container
COPY . /backend

## Uncommend to run a script
#RUN chmod 777 /backend/entrypoint.sh
## run server
#CMD ["./start.sh"]

#RUN apt-get update && apt-get -y install python

# Install the Python libraries
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT FLASK_APP=/backend/run.py flask run --host 0.0.0.0
