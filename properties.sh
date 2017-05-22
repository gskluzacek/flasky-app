# MAIL RELATED CONFIG VALUES
export MAIL_SERVER='xxxx.mail.xxxxhost.com'
export MAIL_PORT='587'
export MAIL_USE_TLS='Y'
export MAIL_USERNAME='xxxx@xxxx.com'
export MAIL_PASSWORD='xxxx'

# APP RELATED EMAIL ADDRESSES
export FLASKY_ADMIN='xxxxx@xxxx.com'
export FLASKY_MAIL_SENDER='xxxx@xxxx.com'

# DB URIs - If not defined will pick up the environment specific config obj default values
# export DEV_DATABASE_URL='data-xxxx.sqlite'
# export TEST_DATABASE_URL='data-xxxx.sqlite'
# export DATABASE_URL='data.sqlite'

# Secret Key - If not defined will pick up the base config object default value
# export SECRET_KEY='xxx'

# controls which config class is used
# see `config` dictionary object in config.py for valid values
export FLASK_CONFIG='development'
