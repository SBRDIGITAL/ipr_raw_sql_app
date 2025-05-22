from sqlite3 import IntegrityError

from .base import BaseDAO

from core.db.enums import *
from core.db.mapping import UserTableFields
from core.db.schemas import UserSchema


class UserDAOSql:

    # Создание пользователя
    CREATE_USER = """
        INSERT INTO {table_name}
        ({field_1}, {field_2}, {field_3}, {field_4})
        VALUES (?, ?, ?, ?)
    """


class UserDAO(BaseDAO):
    
    def __init__(self) -> None:
        super().__init__()
        self.table_name: TableNames = 'users'
        
    def get_users(self):
        """
        ## Получение всех пользователей.

        Returns:
            list: Список пользователей из базы данных.
        """
    
    def insert_user(self, user: UserSchema):
        """
        ## Вставка нового пользователя в базу данных.

        Args:
            user (UserSchema): Схема пользователя, содержащая информацию о новом пользователе.

        Raises:
            IntegrityError: Если возникает ошибка целостности (например, дублирование уникального поля).
            Exception: Для обработки других исключений.
        """
        try:
            query = UserDAOSql.CREATE_USER.format(
                table_name=self.table_name,
                    field_1=UserTableFields.FIRST_NAME,
                    field_2=UserTableFields.EMAIL,
                    field_3=UserTableFields.REG_DATE,
                    field_4=UserTableFields.IS_ACTIVE,
            )
            self.cursor.execute(query, (user.name, user.email, user.registration_date, user.is_active))
            self.connection.commit()
        
        except (IntegrityError, Exception):
            raise
    
    def update_user(self):
        """
        ## Обновление информации о пользователе.

        Raises:
            NotImplementedError: Метод еще не реализован.
        """
        pass
    
    def get_user(self):
        """
        ## Получение информации о конкретном пользователе.

        Raises:
            NotImplementedError: Метод еще не реализован.
        """
        pass
    
    def delete_user(self):
        """
        ## Удаление пользователя из базы данных.

        Raises:
            NotImplementedError: Метод еще не реализован.
        """
        pass
    
    def insert_users(self):
        """
        ## Вставка нескольких пользователей в базу данных.

        Raises:
            NotImplementedError: Метод еще не реализован.
        """
        pass
    
    def update_users(self):
        """
        ## Обновление информации о нескольких пользователях.

        Raises:
            NotImplementedError: Метод еще не реализован.
        """
        pass
    
    def delete_users(self):
        """
        ## Удаление нескольких пользователей из базы данных.

        Raises:
            NotImplementedError: Метод еще не реализован.
        """
        pass



user_dao = UserDAO()