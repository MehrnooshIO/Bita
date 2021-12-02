# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, ARRAY
# from sqlalchemy.orm import relationship
# from db import Base
# from datetime import datetime
# from v_0_1_0.core.models.user import User


# class Post(Base):
#     __tablename__ = 'posts'
#     id = Column(Integer, primary_key=True)
#     title = Column(String(100), nullable=False)
#     content = Column(String(1000), nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     last_updated_at = Column(DateTime, default=datetime.utcnow)
#     # user_id = Column(Integer, ForeignKey('users.id'))
#     # user = relationship(User)
#     tags = ARRAY(String(100))