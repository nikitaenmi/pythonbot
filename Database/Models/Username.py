from Database import Base
from sqlalchemy import Column, Integer, String

class UserID(Base):
    __tablename__ = 'user_id'

    id_username= Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String)
