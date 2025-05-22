from typing import Optional
from sqlite3 import IntegrityError

from core.db.client import DataBase



class BaseDAO(DataBase):
    """
    ## Базовый `Data Access Object` класс для работы с базой данных.

    Args:
        DataBase (DataBase): Базовый класс для работы с базой данных.
    """

    def __init__(self, db_name: str = 'raw_ipr') -> None:
        """
        ## Инициализация базового `DAO`.

        Args:
            db_name (str): Имя базы данных. По умолчанию `'raw_ipr'`.
        """   
        super().__init__(db_name)
    
    def get_all(self, sql: str) -> list[tuple]:
        """
        ## Получение всех записей по `SQL`-запросу.

        Args:
            sql (str): `SQL`-запрос для получения данных.

        Returns:
            list[tuple]: Список кортежей с данными.
        """
        try:
            cur = self.cursor.execute(sql)
            data = cur.fetchall()
            self.connection.commit()
            return data

        except (IntegrityError, Exception):
            self.connection.rollback()
            raise
    
    def insert_one(self, sql: str, parameters: tuple = ()) -> tuple:
        """
        ## Вставка одной записи в базу данных.

        Args:
            sql (str): `SQL`-запрос для вставки данных.
            parameters (tuple): Параметры для `SQL`-запроса. Defaults to ().

        Returns:
            tuple: Кортеж с данными вставленной записи.
        """ 
        try:
            cur = self.cursor.execute(sql, parameters)
            data = cur.fetchone()
            self.connection.commit()
            return data

        except (IntegrityError, Exception):
            self.connection.rollback()
            raise
        
    def update_one(self, sql: str, parameters: tuple = ()) -> tuple:
        """
        ## Обновление одной записи в базе данных.

        Args:
            sql (str): `SQL`-запрос для обновления данных.
            parameters (tuple): Параметры для `SQL`-запроса. Defaults to ().

        Returns:
            tuple: Кортеж с обновленными данными.
        """       
        try:
            cur = self.cursor.execute(sql, parameters)
            data = cur.fetchone()
            self.connection.commit()
            return data

        except (IntegrityError, Exception):
            self.connection.rollback()
            raise
        
    def get_one(self, sql: str, parameters: tuple = ()) -> tuple:
        """
        ## Получение одной записи по `SQL`-запросу.

        Args:
            sql (str): `SQL`-запрос для получения данных.
            parameters (tuple): Параметры для `SQL`-запроса. Defaults to ().

        Returns:
            tuple: Кортеж с данными одной записи.
        """
        try:
            cur = self.cursor.execute(sql, parameters)
            data = cur.fetchone()
            self.connection.commit()
            return data
        
        except Exception as ex:
            raise ex
    
    def delete_one(self, sql: str, parameters: tuple = ()) -> tuple:
        """
        ## Удаление одной записи из базы данных.

        Args:
            sql (str): `SQL`-запрос для удаления `данных`.
            parameters (tuple): Параметры для `SQL`-запроса. Defaults to ().

        Returns:
            tuple: Кортеж с данными удаленной записи.
        """     
        try:
            cur = self.cursor.execute(sql, parameters)
            data = cur.fetchone()
            self.connection.commit()
            return data

        except (IntegrityError, Exception):
            self.connection.rollback()
            raise
    
    def insert_many(self, sql: str, parameters: tuple = (), size: Optional[int] = 1) -> list[tuple]:
        """
        ## Вставка нескольких записей в базу данных.

        Args:
            sql (str): `SQL`-запрос для вставки данных.
            parameters (tuple): Параметры для `SQL`-запроса. Defaults to ().
            size (Optional[int]): Количество записей для вставки. Defaults to 1.

        Returns:
            List[tuple]: Список кортежей с данными вставленных записей.
        """
        try:
            cur = self.cursor.execute(sql, parameters)
            data = cur.fetchmany(size)
            self.connection.commit()
            return data

        except (IntegrityError, Exception):
            self.connection.rollback()
            raise
    
    def update_many(self, sql: str, parameters: tuple = (), size: Optional[int] = 1) -> list[tuple]:
        """
        ## Обновление нескольких записей в базе данных.

        Args:
            sql (str): `SQL`-запрос для обновления данных.
            parameters (tuple): Параметры для `SQL`-запроса. Defaults to ().
            size (Optional[int]): Количество записей для обновления. Defaults to 1.

        Returns:
            List[tuple]: Список кортежей с обновленными данными.
        """
        try:
            cur = self.cursor.execute(sql, parameters)
            data = cur.fetchmany(size)
            self.connection.commit()
            return data

        except (IntegrityError, Exception):
            self.connection.rollback()
            raise
    
    def delete_many(self, sql: str, parameters: tuple = (), size: Optional[int] = 1) -> list[tuple]:
        """
        ## Удаление нескольких записей из базы данных.

        Args:
            sql (str): `SQL`-запрос для удаления данных.
            parameters (tuple): Параметры для `SQL`-запроса. Defaults to ().
            size (Optional[int]): Количество записей для удаления. Defaults to 1.

        Returns:
            List[tuple]: Список кортежей с данными удаленных записей.
        """
        try:
            cur = self.cursor.execute(sql, parameters)
            data = cur.fetchmany(size)
            self.connection.commit()
            return data

        except (IntegrityError, Exception):
            self.connection.rollback()
            raise



base_dao = BaseDAO()