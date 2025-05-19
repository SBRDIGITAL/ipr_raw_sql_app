from .base import BaseDAO
from core.db.enums import PayMethods, TableNames



class PaymentDAO(BaseDAO):
    
    def __init__(self) -> None:
        super().__init__()
        self.table_name: TableNames = 'payments'
        
    def get_payments(self):
        pass    
    
    def insert_payment(self):
        pass
    
    def update_payment(self):
        pass
    
    def get_payment(self):
        pass
    
    def delete_payment(self):
        pass
    
    def insert_payments(self):
        pass
    
    def update_payments(self):
        pass
    
    def delete_payments(self):
        pass



payment_dao = PaymentDAO()