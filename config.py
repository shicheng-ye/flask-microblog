import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['yeeesc@foxmail.com']
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'es', 'zh'] # Web browser only accepts 'zh' and 'zh-CN', while baber accepts 'zh', 'zh-Hans-CN'
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY') # Not MS but Baidu
    MS_TRANSLATOR_ID = os.environ.get('MS_TRANSLATOR_ID')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')