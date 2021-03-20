import os


class Config(object):
    API_VERSION = 'v1'
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
