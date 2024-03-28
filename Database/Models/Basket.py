from Database import Base
from sqlalchemy import Column, Integer, String

class Basket(Base):
    __tablename__ = 'basket'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(String)
