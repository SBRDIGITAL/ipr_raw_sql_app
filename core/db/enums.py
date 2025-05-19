from typing import Literal
from enum import Enum


# Названия таблиц
TableNames = Literal['users', 'orders', 'payments']


class OrderStatus(Enum):
    """
    ## Статусы заказов.

    Args:
        Enum (Enum): Базовый класс для перечислений.
    
    Атрибуты:
        CREATED (int): Статус заказа, созданного, но еще не обработанного.
        PENDING (int): Статус заказа, находящегося в процессе обработки.
        DONE (int): Статус заказа, который был успешно выполнен.
    """   
    CREATED = 1
    PENDING = 2
    DONE = 3
    
    
class PayMethods(Enum):
    """
    ## Методы оплаты.

    Args:
        Enum (Enum): Базовый класс для перечислений.
    
    Атрибуты:
        CREDIT_CARD (int): Метод оплаты с использованием кредитной карты.
        CASH (int): Метод оплаты наличными.
    """    
    CREDIT_CARD = 1
    CASH = 2