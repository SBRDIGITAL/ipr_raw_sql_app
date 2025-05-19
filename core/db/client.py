from traceback import print_exc

from sqlite3 import connect
from sqlite3 import Cursor, Connection

from .models import ALL_TABLES



class DataBase:
    """
    ## Класс для работы с базой данных `SQLite`.

    Этот класс управляет подключением к базе данных, созданием таблиц и выполнением запросов.
    """
    def __init__(self, db_name: str = 'db_name') -> None:
        """
        ## Инициализация класса `DataBase`.

        Создаёт подключение к базе данных и инициализирует курсор.

        Args:
            db_name (str): Имя базы данных. По умолчанию `'db_name'`.
        """        
        self.db_name = db_name + '.db'
        self.connection: Connection = connect(self.db_name)
        self.cursor: Cursor = self.connection.cursor()
        self.__post_init_()
        
    def __post_init_(self):
        """ 
        ## Вызывает методы, необходимые для работы класса.

        Этот метод вызывается после инициализации объекта и отвечает за создание таблиц.
        """
        self.__create_tables()
    
    def __create_tables(self):
        """ 
        ## Создаёт таблицы в базе данных.

        Этот метод выполняет `SQL`-скрипты для создания таблиц, определённых в `ALL_TABLES`.
        """
        def _create(t: str):
            try:
                self.cursor.executescript(t)
                self.connection.commit()
            except:
                print_exc()
                self.connection.rollback()
        [_create(table) for table in ALL_TABLES]
        


db = DataBase('raw_ipr')