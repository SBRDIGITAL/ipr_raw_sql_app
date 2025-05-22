from datetime import date, datetime

from core.dao.users import user_dao, UserDAO

from core.db.schemas import UserSchema




class UserClient:

    def __init__(self) -> None:
        self.dao: UserDAO = user_dao

    def create_user(self):
        self.dao.insert_user(user=UserSchema(
            name='Компьюктер',
            email='popa@example.com',
            registration_date=datetime.now().date(),
            is_active=True
        ))

    def start(self):
        self.create_user()


user_client = UserClient()