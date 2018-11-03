import os

class Config(object):
	SECRET_KEY = ''
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USE_SSL = False
	MAIL_USERNAME = 'Adoa.2018.unla@gmail.com'
	MAIL_PASSWORD = 'adoa.2018*'

class DevelopmentConfig(Config):
	DEBUG = True
	MYSQL_DATABASE_HOST = 'localhost'
	MYSQL_DATABASE_USER = 'root'
	MYSQL_DATABASE_PASSWORD = 'proyecto'
	MYSQL_DATABASE_DB = 'mydb'
		