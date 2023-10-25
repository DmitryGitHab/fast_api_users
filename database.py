from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.interfaces import PoolListener

SQLALCHEMY_URL = "sqlite:///./sql_app.db"
#
# class MyListener():
#     def connect(self, dbapi_connection, connection_record):
#         pass
# engine = create_engine(SQLALCHEMY_URL, listeners=[MyListener()], create_engine={"check_same_tread": False})
# engine = create_engine(SQLALCHEMY_URL, connect_args={"check_same_tread": False})
# engine = create_engine(SQLALCHEMY_URL, connect_args={"check_same_tread": False})
engine = create_engine(SQLALCHEMY_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()