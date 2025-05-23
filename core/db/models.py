from .mapping import *


# Пользователи
CREATE_USER_TABLE = """
    CREATE TABLE IF NOT EXISTS {table_name} (
        {field_id},
        name VARCHAR(50) NOT NULL,
        email VARCHAR(100) UNIQUE,
        registration_date DATE DEFAULT CURRENT_DATE,
        is_active BOOLEAN DEFAULT true,
        {field_updated_at}
    );
""".format(table_name=TablesName.USERS, **ALL_STATIC_FIELDS)


# Заказы ссылаются на пользователей
CREATE_ORDERS_TABLE = """
    CREATE TABLE IF NOT EXISTS {table_name} (
        {field_id},
        user_id INT NOT NULL,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        total_amount DECIMAL(10,2),
        status INTEGER,
        {field_updated_at},
        CONSTRAINT fk_orders_users 
            FOREIGN KEY (user_id) 
            REFERENCES users(id)
            ON DELETE CASCADE
    );
""".format(table_name=TablesName.ORDERS, **ALL_STATIC_FIELDS)



# Кортеж с запросами на создание таблицы
ALL_TABLES: tuple[
    str,
    str,
] = (
    CREATE_USER_TABLE,
    CREATE_ORDERS_TABLE,
)