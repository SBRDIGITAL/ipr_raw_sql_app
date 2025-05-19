from core.db.client import DataBase
from core.db.enums import TableNames



class BaseDAO(DataBase):
    
    def __init__(self, db_name: str = 'raw_ipr') -> None:
        super().__init__(db_name)
    
    def get_all(self, table: TableNames):
        pass    
    
    def insert_one(self, table: TableNames):
        pass
    
    def update_one(self, table: TableNames):
        pass
    
    def get_one(self, table: TableNames):
        pass
    
    def delete_one(self, table: TableNames):
        pass
    
    def insert_many(self, table: TableNames):
        pass
    
    def update_many(self, table: TableNames):
        pass
    
    def delete_many(self, table: TableNames):
        pass



base_dao = BaseDAO()