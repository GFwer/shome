from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from conf import sqlecho

Base = declarative_base()
engine1 = create_engine('mysql+mysqlconnector://root:950828@0.0.0.0/mysql?charset=utf8', echo=sqlecho)
DBSession1 = sessionmaker(bind=engine1)
session = DBSession1()
try:
    session.execute('use mysql')
    session.execute('create database CampusPost')
except Exception as a:
    print(a)
    print('database repeat!')
finally:
    session.close()
engine = create_engine('mysql+mysqlconnector://root:950828@0.0.0.0/CampusPost?charset=utf8', echo=sqlecho)
DBSession = sessionmaker(bind=engine)

