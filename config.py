import os
basedir = os.path.abspath(os.path.dirname(__file__))


# common function to check if a value is True or False
# for use with values read in from Environment Variables
# where real boolean values do not exist and everything
# is a string...
def chk_bool(v):
	return v is not None and str(v).upper() in ('Y', 'YES', 'T', 'TRUE', 'ON', '1')


# environment variables used
#	SECRET_KEY
#	MAIL_SERVER
#	MAIL_PORT
#	MAIL_USE_TLS
#	MAIL_USERNAME
#	MAIL_PASSWORD
#	FLASKY_MAIL_SENDER
#	FLASKY_ADMIN
#	DEV_DATABASE_URL
#	TEST_DATABASE_URL
#	DATABASE_URL


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MAIL_SERVER = 'smtp.googlemail.com'
    #   only using the one mail server right now, so get it from the properties file
    #   in the case of a live production application, there would be per environment
    #   config values for the mail server
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = 587
    MAIL_PORT = os.environ.get('MAIL_PORT')
    # MAIL_USE_TLS = True
    MAIL_USE_TLS = chk_bool(os.environ.get('MAIL_USE_TLS'))
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_MAIL_SENDER = os.environ.get('FLASKY_MAIL_SENDER')
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_POSTS_PER_PAGE = 5
    FLASKY_FOLLOWERS_PER_PAGE = 5
    FLASKY_COMMENTS_PER_PAGE = 5

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
