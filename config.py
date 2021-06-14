class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///dev_db.sqlite3'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://sxdsvvmy:P4M9_LlXXoxe-Jpgm1JpLKlJcROzPAPj@arjuna.db.elephantsql.com:5432/sxdsvvmy'
    MYSQL_CHARSET = 'utf8mb4'
