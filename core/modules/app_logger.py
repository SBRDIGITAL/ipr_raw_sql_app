import logging
from logging import Logger


def setup_logger(filename: str = 'app'):
    filename += '.log'
    logging.basicConfig(
        filename='app.log',  # Имя файла для логов
        level=logging.INFO,   # Уровень логирования
        format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'  # Формат логов
    )
    logger = logging.getLogger()  # Получение корневого логгера
    return logger


app_logger = setup_logger()