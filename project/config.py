import os
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

class Config:
    SECRET_KEY = config('SECRET_KEY')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = config('EMAIL_USER')
    MAIL_PASSWORD = config('EMAIL_PASS')
