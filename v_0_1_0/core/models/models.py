from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey, ARRAY,
    create_engine
)
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from configparser import ConfigParser
from datetime import datetime


config = ConfigParser()
config.read(".env")
_DB_URI = f"postgresql://{config['DATABASE']['USER']}:{config['DATABASE']['PASSWORD']}@{config['DATABASE']['HOST']}:{config['DATABASE']['PORT']}/{config['DATABASE']['NAME']}"

engine = create_engine(_DB_URI)
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.create_all(engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(300), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_updated_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")
    tags = ARRAY(String(100))
