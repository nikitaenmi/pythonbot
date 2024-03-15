from Database import Base
from sqlalchemy import Column, Integer, String

class Username(Base):
    __tablename__ = 'username'

    id_username= Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)