# Маппинги названий таблиц и полей этих таблиц


class TablesName:
    """ 
    ## Названия таблиц в базе данных.
    
    Attributes:
        USERS (str): Название таблицы пользователей.
        ORDERS (str): Название таблицы заказов.
        PAYMENTS (str): Название таблицы платежей.
    """
    USERS = 'users'
    ORDERS = 'orders'
    PAYMENTS = 'payments'    


class StaticFields:
    """
    ## Статичные поля, которые присутствуют во всех таблицах.
    
    Attributes:
        ID (str): Уникальный идентификатор записи.
        CREATED_AT (str): Дата и время создания записи.
        UPDATED_AT (str): Дата и время последнего обновления записи.
    """   
    ID = 'id'
    CREATED_AT = 'created_at'
    UPDATED_AT = 'updated_at'


ALL_STATIC_FIELDS = {  # Описание статичных полей
    'field_id': f'{StaticFields.ID} INTEGER PRIMARY KEY',
    'field_created_at': f'{StaticFields.CREATED_AT} TIMESTAMP DEFAULT CURRENT_TIMESTAMP',
    'field_updated_at': f'{StaticFields.UPDATED_AT} TIMESTAMP DEFAULT CURRENT_TIMESTAMP',
}


class UserTableFields(StaticFields):
    """
    ## Маппинги полей таблицы пользователей.

    Args:
        StaticFields (StaticFields): Статичные поля, унаследованные от класса `StaticFields`.
    
    Attributes:
        ID (str): Уникальный идентификатор записи (Унаследован).
        FIRST_NAME (str): Имя пользователя.
        EMAIL (str): Электронная почта пользователя.
        REG_DATE (str): Дата регистрации пользователя.
        IS_ACTIVE (str): Статус активности пользователя.
        CREATED_AT (str): Дата и время создания записи (Унаследован).
        UPDATED_AT (str): Дата и время последнего обновления записи (Унаследован).
    """   
    FIRST_NAME = 'name'
    EMAIL = 'email'
    REG_DATE = 'registration_date'
    IS_ACTIVE = 'is_active'


class OrdersTableFields(StaticFields):
    """
    ## Маппинги полей таблицы заказов.

    Args:
        StaticFields (StaticFields): Статичные поля, унаследованные от класса `StaticFields`.
    
    Attributes:
        ID (str): Уникальный идентификатор записи (Унаследован).
        USER_ID (str): Идентификатор пользователя, сделавшего заказ.
        ORDER_DATE (str): Дата заказа.
        TOTAL_AMOUNT (str): Общая сумма заказа.
        STATUS (str): Статус заказа.
        CREATED_AT (str): Дата и время создания записи (Унаследован).
        UPDATED_AT (str): Дата и время последнего обновления записи (Унаследован).
    """  
    USER_ID = 'user_id'
    ORDER_DATE = 'order_date'
    TOTAL_AMOUNT = 'total_amount'
    STATUS = 'status'


class PaymentsTableFields(StaticFields):
    """
    ## Маппинги полей таблицы платежей.

    Args:
        StaticFields (StaticFields): Статичные поля, унаследованные от класса `StaticFields`.
    
    Attributes:
        ID (str): Уникальный идентификатор записи (Унаследован).
        ORDER_ID (str): Идентификатор заказа, к которому относится платеж.
        PAYMENT_DATE (str): Дата платежа.
        PAY_METHOD (str): Метод оплаты.
        CREATED_AT (str): Дата и время создания записи (Унаследован).
        UPDATED_AT (str): Дата и время последнего обновления записи (Унаследован).
    """  
    ORDER_ID = 'order_id'
    PAYMENT_DATE = 'payment_date'
    PAY_METHOD = 'payment_method'