import time
import logging
from functools import wraps

logging.basicConfig(
    filename='execution_time.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    encoding='utf-8'
)


def execution_time(func) -> callable:
    """
    Декоратор для измерения времени выполнения функции.

    :param func: Декорируемая функция.
    :return: Обернутая функция.
    """

    @wraps(func)  # Сохраняем метаданные
    def wrapper(*args, **kwargs) -> any:
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            result = None
            error_message = f"Ошибка в функции {func.__name__}: {e}"
            logging.error(error_message)
        end_time = time.time()
        res_time = end_time - start_time

        if result is not None:
            info_message = f"Функция {func.__name__} выполнилась за {res_time:.4f} секунд"
            logging.info(info_message)
        return result

    return wrapper
