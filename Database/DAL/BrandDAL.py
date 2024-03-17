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
            res = session.execute(text("SELECT * FROM brand"))
            for i in range(len(res.all())):
                res = session.execute(text("SELECT * FROM brand"))
                if res.all()[i][1] == name:
                    return True, print("True")
                else:
                    return False, print("False")










