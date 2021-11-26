from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///blog.sqlite3')
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

Base.metadata.create_all(engine)