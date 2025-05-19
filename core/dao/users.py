from .base import BaseDAO
from core.db.enums import *



class UserDAO(BaseDAO):
    
    def __init__(self) -> None:
        super().__init__()
        self.table_name: TableNames = 'users'
        
    def get_users(self):
        pass    
    
    def insert_user(self):
        pass
    
    def update_user(self):
        pass
    
    def get_user(self):
        pass
    
    def delete_user(self):
        pass
    
    def insert_users(self):
        pass
    
    def update_users(self):
        pass
    
    def delete_users(self):
        pass



user_dao = UserDAO()