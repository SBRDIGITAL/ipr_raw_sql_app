from .base import BaseDAO
from core.db.enums import OrderStatus, TableNames



class OrderDAO(BaseDAO):
    
    def __init__(self) -> None:
        super().__init__()
        self.table_name: TableNames = 'orders'
        
    def get_orders(self):
        pass    
    
    def insert_order(self):
        pass
    
    def update_order(self):
        pass
    
    def get_order(self):
        pass
    
    def delete_order(self):
        pass
    
    def insert_orders(self):
        pass
    
    def update_orders(self):
        pass
    
    def delete_orders(self):
        pass



order_dao = OrderDAO()