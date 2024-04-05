from Database import Base
from sqlalchemy import Column, Integer, String

class Basket(Base):
    __tablename__ = 'basket'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sneaker_id = Column(String)
    quantity = Column(Integer)
    size = Column(Integer)
    user_id = Column(Integer)



