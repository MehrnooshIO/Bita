from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from configparser import ConfigParser


config = ConfigParser()
config.read(".env")
_DB_URI = f"postgresql://{config['DATABASE']['USER']}:{config['DATABASE']['PASSWORD']}@{config['DATABASE']['HOST']}:{config['DATABASE']['PORT']}/{config['DATABASE']['NAME']}"

engine = create_engine(_DB_URI)
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.create_all(engine)
