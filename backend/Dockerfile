#FROM Ubuntu
#FROM python:alpine3.7
FROM python:3.6.2

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app

# Update working directory
WORKDIR /usr/src/app

# to create a user
#ARG username
#RUN adduser -D ${username}
#RUN chown -R ${username} /app
#USER ${username}

# copy everything from this directory to server/flask docker container
COPY . /usr/src/app/

# Give execute permission to below file, so that the script can be executed by docker.
RUN chmod 777 /usr/src/app/entrypoint.sh

#RUN apt-get update && apt-get -y install python

# Install the Python libraries
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# run server
#CMD ["./entrypoint.sh"]

#COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/run.py flask run