from Database.Models.Brand import Brand
from Database.config import Session
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




