from datetime import datetime
from pydoc import cli

from core.dao.users import user_dao, UserDAO

from core.db.schemas import SomeOrder, UserSchema, UserUpdate, SomeUser

from .orders import OrdersClient


class UserClient:
    """
    ## Клиент для работы с пользователями.

    Предоставляет методы для создания, обновления, получения и удаления пользователей.

    Attributes:
        dao (UserDAO): Объект `DAO` для взаимодействия с базой данных.
    """
    def __init__(self) -> None:
        """
        ## Инициализация клиента пользователей.

        Создает экземпляр `UserClient` и инициализирует `DAO` для работы с пользователями.
        """
        self.dao: UserDAO = user_dao

    def create_user(self) -> SomeUser:
        """
        ## Создание нового пользователя.

        Создает нового пользователя с предопределенными данными и сохраняет его в базе данных.

        Returns:
            SomeUser: Созданный пользователь.
        """
        return self.dao.insert_user(
            UserSchema(
                name='test_user',
                email='popa@example.com',
                registration_date=datetime.now().date(),
                is_active=True,
            )
        )

    def update_user(self, id: int) -> SomeUser:
        """
        ## Обновление информации о пользователе.

        Обновляет информацию о пользователе с заданным идентификатором.

        Args:
            id (int): Идентификатор пользователя, информацию о котором нужно обновить.

        Returns:
            SomeUser: Обновленный пользователь.
        """
        return self.dao.update_user(UserUpdate(name='now_this_user_updated'), id=id)

    def start_orders_client(self, user_id: int):
        client = OrdersClient(user_id)
        client.start()

    def start(self):
        """
        ## Запуск клиента пользователей.

        ### Алгоритм:
            - Создает нового пользователя.
            - обновляет его информацию.
            - получает пользователя по идентификатору.
            - получает всех пользователей.
            - удаляет обновленного пользователя.
            - Выводит информацию о всех операциях в консоль.
        """  
        created_user: SomeUser = self.create_user()
        updated_user: SomeUser = self.update_user(id=created_user.id)
        user_by_id: SomeUser = self.dao.get_user(id=updated_user.id)
        all_users: list[SomeUser] = self.dao.get_users()

        self.start_orders_client(updated_user.id)

        deleted_user: SomeUser = self.dao.delete_user(id=updated_user.id)
        print(f'\n\n***************** ПОЛЬЗОВАТЕЛИ *****************')
        print(f'\n{created_user=}')
        print(f'\n{updated_user=}')
        print(f'\n{user_by_id=}')
        print(f'\n{all_users=}')
        print(f'\n{deleted_user=}\n\n')

        print(f'\n\n***************** СОЗДАЁМ ПОЛЬЗОВАТЕЛЯ, ДОБАВЛЯЕМ ЗАКАЗ, УДАЛЯЕМ ПОЛЬЗОВАТЕЛЯ ДЛЯ КАСКАДНОГО УДАЛЕНИЯ *****************')
        created_user: SomeUser = self.create_user()
        client = OrdersClient(user_id=created_user.id)
        crearted_order: SomeOrder = client.create_order()
        deleted_user: SomeUser = self.dao.delete_user(id=updated_user.id)
        all_orders: list[SomeOrder] = client.dao.get_orders()
        print(f'\n{created_user=}')
        print(f'\n{crearted_order=}')
        print(f'\n{deleted_user=}')
        print(f'\n{all_orders=}')



user_client = UserClient()