from sqlite3 import IntegrityError
from unittest import result

from .base import BaseDAO

from core.db.enums import TableNames
from core.db.schemas import OrdersSchema, SomeOrder, UpdateOrder
from core.db.mapping import OrdersTableFields


from .sql_templates import *



class OrderDAO(BaseDAO):
    """
    ## Класс для работы с заказами в базе данных.

    Наследуется от `BaseDAO` и предоставляет методы для выполнения операций `CRUD` с заказами.
    """
    def __init__(self) -> None:
        """
        ## Инициализация `OrderDAO`.

        Устанавливает имя таблицы заказов.
        """
        super().__init__()
        self.table_name: TableNames = 'orders'
        
    def get_orders(self) -> list[SomeOrder]:
        """
        ## Получение всех заказов.

        Выполняет запрос к базе данных для получения всех заказов.

        Returns:
            list[SomeOrder]: Список заказов из базы данных.

        Raises:
            IntegrityError: Если возникает ошибка целостности.
            Exception: Для обработки других исключений.
        """
        try:
            result = self.get_all(GET_ALL.format(table_name=self.table_name))
            data = [
                SomeOrder(
                    id=i[0],
                    user_id=i[1],
                    order_date=i[2],
                    total_amount=i[3],
                    status=i[4]
                ) for i in result
            ]
            return data

        except (IntegrityError, Exception):
            raise
    
    def insert_order(self, order: OrdersSchema) -> SomeOrder:
        """
        ## Вставка нового заказа в базу данных.

        Args:
            order (OrdersSchema): Схема заказа, содержащая информацию о новом заказе.

        Returns:
            SomeOrder: Созданный заказ.

        Raises:
            IntegrityError: Если возникает ошибка целостности (например, дублирование уникального поля).
            Exception: Для обработки других исключений.
        """
        try:
            query = CREATE_ONE.format(
                table_name=self.table_name,
                    field_1=OrdersTableFields.USER_ID,
                    field_2=OrdersTableFields.ORDER_DATE,
                    field_3=OrdersTableFields.TOTAL_AMOUNT,
                    field_4=OrdersTableFields.STATUS,
            )
            data = self.insert_one(query, (order.user_id, order.order_date, order.total_amount, order.status))
            return SomeOrder(
                id=data[0],
                user_id=data[1],
                order_date=data[2],
                total_amount=data[3],
                status=data[4]
            )

        except (IntegrityError, Exception):
            raise
    
    def update_order(self, order: UpdateOrder, id: int) -> SomeOrder:
        """
        ## Обновление информации о заказе.

        Args:
            order (UpdateOrder): Обновленная информация о заказе.
            id (int): Идентификатор заказа, который нужно обновить.

        Returns:
            SomeOrder: Обновленный заказ.

        Raises:
            IntegrityError: Если возникает ошибка целостности.
            Exception: Для обработки других исключений.
        """
        try:
            up_order = order.model_dump(exclude_unset=True)
            cortege = up_order.values()
            query = UPDATE_ONE.format(
                table_name=self.table_name,
                    field_1=OrdersTableFields.ORDER_DATE,
                    main_field=OrdersTableFields.ID
            )
            data = self.update_one(query, (*cortege, id))
            return SomeOrder(
                id=data[0],
                user_id=data[1],
                order_date=data[2],
                total_amount=data[3],
                status=data[4]
            )

        except (IntegrityError, Exception):
            raise
    
    def get_order(self, id: int) -> SomeOrder:
        """
        ## Получение информации о конкретном заказе.

        Args:
            id (int): Идентификатор заказа, информацию о котором нужно получить.

        Returns:
            SomeOrder: Информация о заказе.

        Raises:
            IntegrityError: Если возникает ошибка целостности.
            Exception: Для обработки других исключений.
        """
        try:
            query = GET_ONE.format(
                table_name=self.table_name,
                    main_field=OrdersTableFields.ID
            )
            data = self.get_one(query, (id,))
            return SomeOrder(
                id=data[0],
                user_id=data[1],
                order_date=data[2],
                total_amount=data[3],
                status=data[4]
            )

        except (IntegrityError, Exception):
            raise
    
    def delete_order(self, id: int) -> SomeOrder:
        """
        ## Удаление заказа из базы данных.

        Args:
            id (int): Идентификатор заказа, который нужно удалить.

        Returns:
            SomeOrder: Удаленный заказ.

        Raises:
            IntegrityError: Если возникает ошибка целостности.
            Exception: Для обработки других исключений.
        """        
        try:
            query = DELETE_ONE.format(
                table_name=self.table_name,
                    main_field=OrdersTableFields.ID
            )
            data = self.delete_one(query, (id,))
            return SomeOrder(
                id=data[0],
                user_id=data[1],
                order_date=data[2],
                total_amount=data[3],
                status=data[4]
            )

        except (IntegrityError, Exception):
            raise



order_dao = OrderDAO()