"""
Configure Settings for application for specific environment
"""

import os

class Config(object):
    """ Common config options """
    APPNAME = 'Angular_Flask_Docker_Demo'
    VERSION = '1.0'
    APPID = 'fl_angular_docker'
    SECRET_KEY = os.urandom(24)
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_NATIVE_UNICODE = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('POSTGRES_USER')
    DB_PASS = os.getenv('POSTGRES_PASSWORD')
    DB_SERVICE = os.getenv('DB_SERVICE')
    DB_PORT = os.getenv('DB_PORT')
    BROKER_URL = os.getenv('BROKER_URL')
    CELERY_BACKEND = os.getenv('CELERY_BACKEND')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME)
    print(SQLALCHEMY_DATABASE_URI)


class DevelopmentConfig(Config):
    """ Dev environment config options """
    FLASK_ENV='development'
    DEBUG = True
    PROFILE = True

class TestingConfig(Config):
    """ Testing environment config options """
    DEBUG = False
    STAGING = True
    TESTING = True


class ProductionConfig(Config):
    """ Prod environment config options """
    FLASK_ENV = 'production'
    DEBUG = False
    STAGING = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
