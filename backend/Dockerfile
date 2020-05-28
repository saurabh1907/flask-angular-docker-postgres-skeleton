FROM Ubuntu

RUN apt-get update && apt-get -y install python

RUN pip install flask flask-restful

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/run.py flask run