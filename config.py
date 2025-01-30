import os
import pymysql 

class Config:
    SECRET_KEY ='supersecretkey'
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:@localhost/sekul_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY ='superjwtsecretkey'