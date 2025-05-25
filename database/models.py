from sqlalchemy import Column, Integer

from database.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, default=0)
