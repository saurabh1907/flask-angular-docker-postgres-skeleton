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
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_NATIVE_UNICODE = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    BROKER_URL = 'redis://localhost:6379/0'
    CELERY_BACKEND = 'postgresql://postgres:postgres@localhost:5432/blogs_db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///memory'

class CeleryConfig(Config):
    """ Testing environment config options """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_NATIVE_UNICODE = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DB_NAME = 'blogs_db'
    DB_USER = 'postgres'
    DB_PASS = 'postgres'
    DB_SERVICE = 'localhost'
    DB_PORT = 5432
    BROKER_URL = 'redis://localhost:6379/0'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME)

class ProductionConfig(Config):
    """ Prod environment config options """
    FLASK_ENV = 'production'
    DEBUG = False
    STAGING = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'celery': CeleryConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
