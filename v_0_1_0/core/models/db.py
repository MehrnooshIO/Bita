from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

_DB_URI = 'mysql://root:fiFm3ZAzJddOihQN@services.gen1.chabokan.net:52782/rick'
engine = create_engine(_DB_URI)
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

Base.metadata.create_all(engine)