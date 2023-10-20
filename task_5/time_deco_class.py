import time
import logging
from functools import wraps

logging.basicConfig(
    filename='execution_time.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    encoding='utf-8'
)


class ExecutionTime:
    def __init__(self, func):
        """
        Декоратор для измерения времени выполнения функции и записи результатов в лог.

        :param func: Декорируемая функция.
        """
        self.func = func
        wraps(func)(self)  # Сохраняем метаданные

    def __call__(self, *args, **kwargs):
        """
        Вызывает декорированную функцию, измеряет время её выполнения и записывает результат в лог.

        :param args: Позиционные аргументы для декорированной функции.
        :param kwargs: Именованные аргументы для декорированной функции.
        :return: Результат выполнения декорированной функции.
        """
        start_time = time.time()
        try:
            result = self.func(*args, **kwargs)
        except Exception as e:
            result = None
            error_message = f"Ошибка в функции {self.func.__name__}: {e}"
            logging.error(error_message)
        end_time = time.time()
        res_time = end_time - start_time

        if result is not None:
            info_message = f"Функция {self.func.__name__} выполнилась за {res_time:.4f} секунд"
            logging.info(info_message)
        return result
