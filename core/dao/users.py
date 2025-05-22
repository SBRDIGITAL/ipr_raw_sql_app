from sqlite3 import IntegrityError

from .base import BaseDAO

from core.db.enums import *
from core.db.mapping import UserTableFields
from core.db.schemas import UserSchema, UserUpdate, SomeUser


class UserDAOSql:
    """
    ## Класс, содержащий `SQL`-запросы для работы с пользователями в базе данных.
    """

    # Получение всех пользователей
    GET_ALL = """
        SELECT * FROM {table_name}
    """

    # Получение одного пользователя
    GET_ONE = """
        SELECT * FROM {table_name}
        WHERE {main_field} = ?
    """

    # Создание пользователя
    CREATE_USER = """
        INSERT INTO {table_name}
        ({field_1}, {field_2}, {field_3}, {field_4})
        VALUES (?, ?, ?, ?) 
        RETURNING *
    """

    # Обновление пользователя
    UPDATE_USER = """
        UPDATE {table_name}
        SET {field_1} = ?
        WHERE {main_field} = ?
        RETURNING *
    """

    # Удаление пользователя
    DELETE_USER = """
        DELETE FROM {table_name}
        WHERE {main_field} = ?
        RETURNING *
    """


class UserDAO(BaseDAO):
    """
    ## Класс для работы с пользователями в базе данных.

    Наследуется от `BaseDAO` и предоставляет методы для выполнения операций `CRUD`.
    """

    def __init__(self) -> None:
        """
        ## Инициализация `UserDAO`.

        Устанавливает имя таблицы пользователей.
        """
        super().__init__()
        self.table_name: TableNames = 'users'
        
    def get_users(self) -> list[SomeUser]:
        """
        ## Получение всех пользователей.

        Выполняет запрос к базе данных для получения всех пользователей.

        Returns:
            list[SomeUser]: Список пользователей из базы данных.

        Raises:
            IntegrityError: Если возникает ошибка целостности.
            Exception: Для обработки других исключений.
        """
        try:
            result = self.get_all(UserDAOSql.GET_ALL.format(table_name=self.table_name))
            data = [
                SomeUser(
                    id=i[0],
                    name=i[1],
                    email=i[2],
                    registration_date=i[3],
                    is_active=i[4]
                ) for i in result
            ]
            return data

        except (IntegrityError, Exception):
            raise
    
    def insert_user(self, user: UserSchema) -> SomeUser:
        """
        ## Вставка нового пользователя в базу данных.

        Args:
            user (UserSchema): Схема пользователя, содержащая информацию о новом пользователе.

        Returns:
            SomeUser: Созданный пользователь.

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
            data = self.insert_one(query, (user.name, user.email, user.registration_date, user.is_active))
            return SomeUser(
                id=data[0],
                name=data[1],
                email=data[2],
                registration_date=data[3],
                is_active=data[4]
            )

        except (IntegrityError, Exception):
            raise
    
    def update_user(self, user: UserUpdate, id: int) -> SomeUser:
        """
        ## Обновление информации о пользователе.

        Args:
            user (UserUpdate): Обновленная информация о пользователе.
            id (int): Идентификатор пользователя, которого нужно обновить.

        Returns:
            SomeUser: Обновленный пользователь.

        Raises:
            IntegrityError: Если возникает ошибка целостности.
            Exception: Для обработки других исключений.
        """
        try:
            up_user = user.model_dump(exclude_unset=True)
            cortege = up_user.values()
            query = UserDAOSql.UPDATE_USER.format(
                table_name=self.table_name,
                    field_1=UserTableFields.FIRST_NAME,
                    main_field=UserTableFields.ID
            )
            data = self.update_one(query, (*cortege, id))
            return SomeUser(
                id=data[0],
                name=data[1],
                email=data[2],
                registration_date=data[3],
                is_active=data[4]
            )

        except (IntegrityError, Exception):
            raise
    
    def get_user(self, id: int) -> SomeUser:
        """
        ## Получение информации о конкретном пользователе.

        Args:
            id (int): Идентификатор пользователя, информацию о котором нужно получить.

        Returns:
            SomeUser: Информация о пользователе.

        Raises:
            IntegrityError: Если возникает ошибка целостности.
            Exception: Для обработки других исключений.
        """
        try:
            query = UserDAOSql.GET_ONE.format(
                table_name=self.table_name,
                    main_field=UserTableFields.ID
            )
            data = self.get_one(query, (id,))
            return SomeUser(
                id=data[0],
                name=data[1],
                email=data[2],
                registration_date=data[3],
                is_active=data[4]
            )

        except (IntegrityError, Exception):
            raise
    
    def delete_user(self, id: int) -> SomeUser:
        """
        ## Удаление пользователя из базы данных.

        Args:
            id (int): Идентификатор пользователя, которого нужно удалить.

        Returns:
            SomeUser: Удаленный пользователь.

        Raises:
            IntegrityError: Если возникает ошибка целостности.
            Exception: Для обработки других исключений.
        """
        try:
            query = UserDAOSql.DELETE_USER.format(
                table_name=self.table_name,
                    main_field=UserTableFields.ID
            )
            data = self.delete_one(query, (id,))
            return SomeUser(
                id=data[0],
                name=data[1],
                email=data[2],
                registration_date=data[3],
                is_active=data[4]
            )

        except (IntegrityError, Exception):
            raise



user_dao = UserDAO()