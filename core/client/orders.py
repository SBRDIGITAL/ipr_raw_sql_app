from datetime import datetime, date
from decimal import Decimal

from core.dao.orders import order_dao, OrderDAO
from core.db.enums import OrderStatus
from core.db.schemas import OrdersSchema, SomeOrder, SomeUser, UpdateOrder



class OrdersClient:
    """
    ## Клиент для работы с заказами.

    Предоставляет методы для создания, обновления, получения и удаления заказов.

    Attributes:
        dao (UserDAO): Объект `DAO` для взаимодействия с базой данных.
    """
    def __init__(self, user_id: int) -> None:
        """
        ## Инициализация клиента заказов.

        Создает экземпляр `OrdersClient` и инициализирует `DAO` для работы с заказами.
        """
        self.user_id = user_id
        self.dao: OrderDAO = order_dao

    def create_order(self) -> SomeOrder:
        return self.dao.insert_order(
            OrdersSchema(
                user_id=self.user_id,
                order_date=datetime.now().date(),
                total_amount=float(Decimal(3.0)),
                status=OrderStatus.CREATED.value
            )
        )

    def update_order(self, id: int) -> SomeOrder:
        """
        ## _summary_.

        Args:
            id (int): _description_.

        Returns:
            SomeOrder: _description_.
        """        
        return self.dao.update_order(
            UpdateOrder(
                order_date=date(year=1970, month=1, day=1),
            ),
            id=id 
        )

    def start(self):
        """
        ## Запуск клиента заказов.

        ### Алгоритм:
            - Создает новый заказ.
            - обновляет его информацию.
            - получает заказ по идентификатору.
            - получает все заказы.
            - удаляет обновленный заказ.
            - Выводит информацию о всех операциях в консоль.
        """
        created_order: SomeOrder = self.create_order()
        updated_order: SomeOrder = self.update_order(id=created_order.id)
        order_by_id: SomeOrder = self.dao.get_order(id=updated_order.id)
        all_orders: list[SomeOrder] = self.dao.get_orders()
        deleted_order: SomeOrder = self.dao.delete_order(id=updated_order.id)
        print(f'\n\n***************** ЗАКАЗЫ *****************')
        print(f'\n{created_order=}')
        print(f'\n{updated_order=}')
        print(f'\n{order_by_id=}')
        print(f'\n{all_orders=}')
        print(f'\n{deleted_order=}')



# orders_client = OrdersClient()