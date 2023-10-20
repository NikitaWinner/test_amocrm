import os
import logging


def generate_directory_tree(path: str, depth: int = 0, indent: str = '    ') -> None:
    """
    Рекурсивно выводит структуру папок и файлов в дереве, начиная с указанного пути.

    :param path: Путь к корневой папке, с которой начинается вывод.
    :param depth: Глубина отступов в дереве (по умолчанию 0).
    :param indent: Строка отступа для форматирования (по умолчанию '    ').

    :return: Нет возвращаемого значения. Результат выводится на консоль.
    """
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(f"{indent * depth}[{item}]")
                generate_directory_tree(item_path, depth + 1)
            else:
                print(f"{indent * depth}{item}")
    except FileNotFoundError:
        logging.warning(f"Файл или папка не найдены: {item_path}")
    except PermissionError:
        logging.error(f"Нет разрешения на доступ к: {item_path}")
    except Exception as e:
        logging.error(f"Ошибка: {e}")


if __name__ == '__main__':

    logging.basicConfig(
        filename='tree_1.log',
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s]: %(message)s',
        encoding='utf-8'
    )
    generate_directory_tree("tree_class")
