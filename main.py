from core.db.client import db



class RawSqlApp:
    
    def __init__(self) -> None:
        self.db = db

    def start(self):
        pass



if __name__ == '__main__':
    rsa = RawSqlApp()
    rsa.start()