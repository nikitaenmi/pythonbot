from Database.Models.Brand import Brand
from Database.config import Session
from sqlalchemy import text
class BrandDAL:
    @staticmethod
    def new_brand(namebrand):
        with Session() as session:
            new_brand = Brand(namebrand=namebrand)
            session.add(new_brand)
            session.commit()

    @staticmethod
    def delete_brand():
        with Session() as session:
            session.query(Brand).filter(Brand.id_brand == 14).delete()
            session.commit()

    @staticmethod
    def search_brand(name):
        with Session() as session:
            return session.execute(text(f"SELECT * FROM brand WHERE namebrand = '{name}'")).fetchone() is not None

# print(BrandDAL.search_brand("324321"))


#     @staticmethod
#     def search_brand():
#         with Session() as session:
#              res = list(session.execute(text("SELECT * FROM brand")))
#              print(res)
#              print(res)
#
# BrandDAL.search_brand()







