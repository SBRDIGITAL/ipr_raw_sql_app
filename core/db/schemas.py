from datetime import datetime, date
from typing import Annotated, Optional

from pydantic import BaseModel, Field

from core.db.enums import OrderStatus, PayMethods



class StaticFieldsSchema(BaseModel):
    """
    ## Статические поля схемы.

    Args:
        BaseModel (pydantic.BaseModel): Базовая модель Pydantic.

    Attributes:
        id (int): Уникальный идентификатор записи.
        created_at (datetime): Дата и время создания записи.
        updated_at (datetime): Дата и время последнего обновления записи.
    """
    # id: Optional[int]
    # updated_at: datetime = datetime.now()


class UserSchema(StaticFieldsSchema):
    """
    ## Схема пользователя.

    Args:
        StaticFieldsSchema (pydantic.BaseModel): Базовая модель с статическими полями.

    Attributes:
        name (str): Имя пользователя, максимальная длина 50 символов.
        email (str): Электронная почта пользователя, максимальная длина 100 символов.
        registration_date (datetime.date): Дата регистрации пользователя.
        is_active (bool): Статус активности пользователя (по умолчанию True).

    Example:
        >>> user = UserSchema(id=1, name="Иван Иванов", email="ivan@example.com",
        registration_date=datetime.now().date(), is_active=True)
    """
    name: Annotated[str, Field(max_length=50)]
    email: Annotated[str, Field(max_length=100)]
    registration_date: Annotated[date, Field(default=datetime.now().date())]
    is_active: bool = True


class SomeUser(BaseModel):
    """
    ## Модель пользователя.

    Представляет собой модель данных для пользователя с необходимыми полями.

    Args:
        BaseModel (BaseModel): Базовая модель `Pydantic` для валидации данных.
    
    Attributes:
        id (int): Идентификатор пользователя.
        name (str): Имя пользователя.
        email (str): Электронная почта пользователя.
        registration_date (date): Дата регистрации пользователя.
        is_active (bool): Статус активности пользователя.
    """
    id: int
    name: str
    email: str
    registration_date: date
    is_active: bool


class UserUpdate(BaseModel):
    """
    ## Модель обновления пользователя.

    Представляет собой модель данных для обновления информации о пользователе.

    Args:
        BaseModel (BaseModel): Базовая модель `Pydantic` для валидации данных.
    
    Attributes:
        name (Optional[str]): Имя пользователя (опционально).
        email (Optional[str]): Электронная почта пользователя (опционально).
        registration_date (Optional[date]): Дата регистрации пользователя (опционально).
        is_active (Optional[bool]): Статус активности пользователя (опционально).
    """ 
    name: Optional[str] = None
    email: Optional[str] = None
    registration_date: Optional[date] = None
    is_active: Optional[bool] = None



class OrdersSchema(StaticFieldsSchema):
    """
    ## Схема заказа.

    Args:
        StaticFieldsSchema (pydantic.BaseModel): Базовая модель с статическими полями.

    Attributes:
        user_id (int): Уникальный идентификатор пользователя, сделавшего заказ.
        order_date (datetime.date): Дата заказа.
        total_amount (Decimal): Общая сумма заказа.
        status (OrderStatus): Статус заказа.
    
    Example:
    >>> ord_sch = OrdersSchema(id=1, user_id=1, order_date=datetime.now().date(),
        total_amount=Decimal(10.2), status=OrderStatus.CREATED)
    """
    user_id: int
    order_date: date
    total_amount: float
    status: int


class SomeOrder(StaticFieldsSchema):
    """
    ## Модель для представления заказа.

    Хранит информацию о заказе, включая идентификатор,
    идентификатор пользователя, дату заказа, общую сумму и статус.
    """
    id: int
    user_id: int
    order_date: date
    total_amount: float
    status: int


class UpdateOrder(StaticFieldsSchema):
    """
    ## Модель для обновления информации о заказе.

    Позволяет обновлять поля заказа, при этом все поля являются необязательными.
    """
    user_id: Optional[int] = None
    order_date: Optional[date] = None
    total_amount: Optional[float] = None
    status: Optional[int] = None


class PaymentsSchema(StaticFieldsSchema):
    """
    ## Схема платежа.

    Args:
        StaticFieldsSchema (pydantic.BaseModel): Базовая модель с статическими полями.

    Attributes:
        user_id (int): Уникальный идентификатор пользователя, совершившего платеж.
        order_id (int): Уникальный идентификатор заказа, к которому относится платеж.
        payment_date (datetime.date): Дата платежа.
        payment_method (PayMethods): Метод платежа.
    
    Example:
        >>> payment = PaymentsSchema(id=1, user_id=1, order_id=1,
        payment_date=datetime.now().date(), payment_method=PayMethods.CREDIT_CARD)
    """
    user_id: int
    order_id: int
    payment_date: date
    payment_method: PayMethods