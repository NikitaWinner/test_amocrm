import os
import logging
from pathlib import Path
from typing import Generator


def generate_item(entry: os.DirEntry, depth: int, indent: str = '    ') -> Generator[str, None, None]:
    """
    Генерирует отформатированные строки для элементов директории.

    :param entry: Элемент для обработки.
    :param depth: Глубина в дереве директории.
    :param indent: Строка для отступа.
    :return: Отформатированная строка для элемента директории.
    """
    try:
        if entry.is_dir():
            yield f'{indent * depth}[{entry.name}]'
        else:
            yield f'{indent * depth}{entry.name}'

    except FileNotFoundError as e:
        logging.warning(f"Файл или папка не найдены: {entry.name} ({e})")
    except PermissionError as e:
        logging.error(f"Нет разрешения на доступ к: {entry.name} ({e})")
    except Exception as e:
        logging.error(f"Ошибка: {entry.name} ({e})")


def generate_tree(path: str, depth: int = 0) -> Generator[str, None, None]:
    """
    Генерирует представление дерева директории.

    :param path: Путь, с которого начинается дерево.
    :param depth: Текущая глубина в дереве.
    :return: Отформатированная строка для каждого элемента директории.
    """
    try:
        for entry in Path(path).iterdir():
            yield from generate_item(entry, depth)
            if entry is not None and entry.is_dir():
                yield from generate_tree(entry, depth + 1)

    except FileNotFoundError as e:
        logging.warning(f"Файл или папка не найдены: {entry} ({e})")
    except PermissionError as e:
        logging.error(f"Нет разрешения на доступ к: {entry} ({e})")
    except Exception as e:
        logging.error(f"Ошибка: {entry} ({e})")


if __name__ == '__main__':

    logging.basicConfig(
        filename='tree_2.log',
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s]: %(message)s',
        encoding='utf-8'
    )
    tree_generator = generate_tree('tree_yaml')
    for item in tree_generator:
        print(item)
