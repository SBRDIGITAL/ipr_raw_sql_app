from core.db.client import db

from core.client.user import user_client



class RawSqlApp:
    
    def __init__(self) -> None:
        self.db = db

    def start(self):
        user_client.start()


if __name__ == '__main__':
    rsa = RawSqlApp()
    rsa.start()