from core.db.client import DataBase
from core.db.enums import TableNames



class BaseDAO(DataBase):
    
    def __init__(self, db_name: str = 'raw_ipr') -> None:
        super().__init__(db_name)
    
    def get_all(self, table: TableNames):
        try:
            pass
        
        except Exception as ex:
            raise ex
    
    def insert_one(self, table: TableNames):
        try:
            pass
        
        except Exception as ex:
            raise ex
        
    def update_one(self, table: TableNames):
        try:
            pass
        
        except Exception as ex:
            raise ex
        
    def get_one(self, table: TableNames):
        try:
            pass
        
        except Exception as ex:
            raise ex
    
    def delete_one(self, table: TableNames):
        try:
            pass
        
        except Exception as ex:
            raise ex
    
    def insert_many(self, table: TableNames):
        try:
            pass
        
        except Exception as ex:
            raise ex
    
    def update_many(self, table: TableNames):
        try:
            pass

        except Exception as ex:
            raise ex
    
    def delete_many(self, table: TableNames):
        try:
            pass

        except Exception as ex:
            raise ex



base_dao = BaseDAO()