# Получение всех записей из таблицы
GET_ALL = """
    SELECT * FROM {table_name}
"""

# Получение одной записи по условию
GET_ONE = """
    SELECT * FROM {table_name}
    WHERE {main_field} = ?
"""

# Создание одной записи с возвратом всех полей записи
CREATE_ONE = """
    INSERT INTO {table_name}
    ({field_1}, {field_2}, {field_3}, {field_4})
    VALUES (?, ?, ?, ?) 
    RETURNING *
"""

# Обновление одной записи по условию
UPDATE_ONE = """
    UPDATE {table_name}
    SET {field_1} = ?
    WHERE {main_field} = ?
    RETURNING *
"""

# Удаление одной записи
DELETE_ONE = """
    DELETE FROM {table_name}
    WHERE {main_field} = ?
    RETURNING *
"""