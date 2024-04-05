from Database.Models.Brand import Brand
from Database.Models.Username import UserID
from Database.Models.Basket import Basket
from Database.config import Session
from sqlalchemy import text
class BrandDAL:
    @staticmethod
    def new_brand(id):
        with Session() as session:
            new_id = UserID(user_id=id)
            session.add(new_id)
            session.commit()

    @staticmethod
    def delete_brand():
        with Session() as session:
            session.query(Brand).filter(Brand.id_brand == 14).delete()
            session.commit()

    @staticmethod
    def search_basket(id):
        with Session() as session:
            res = session.execute(text(f"SELECT sneaker_id FROM basket WHERE user_id = '{id}'"))
            return(res.all())





    @staticmethod
    def search_brand(id):
        with Session() as session:
            return session.execute(text(f"SELECT * FROM user_id WHERE user_id = '{id}'")).fetchone() is not None

    @staticmethod
    def add_basket(brand, id):
        with Session() as session:
            new_brand_n_id_basket = Basket(sneaker_id = brand,user_id = id)
            session.add(new_brand_n_id_basket)
            session.commit()

# print(BrandDAL.search_brand("324321"))

#     @staticmethod
#     def search_brand():
#         with Session() as session:
#              res = list(session.execute(text("SELECT * FROM brand")))
#              print(res)
#              print(res)
#
# BrandDAL.search_brand()


BrandDAL.search_basket("1175540520")
#BrandDAL.add_basket('test',123132)



BrandDAL.search_basket(1175540520)