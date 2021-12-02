from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

_DB_URI = 'postgresql://root:JhE7DtbmnTdKQ5Sz@services.gen1.chabokan.net:15947/anna'
engine = create_engine(_DB_URI)
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

Base.metadata.create_all(engine)