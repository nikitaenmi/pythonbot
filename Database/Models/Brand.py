from Database import Base
from sqlalchemy import Column, Integer, String

class Brand(Base):
    __tablename__ = 'brand'

    id_brand = Column(Integer, primary_key=True, autoincrement=True)
    namebrand = Column(String)

