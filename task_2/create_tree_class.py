import os
from typing import List
import logging


logging.basicConfig(
    filename='tree_class.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    encoding='utf-8'
)


class Node:
    """
    Класс, представляющий узел дерева файловой структуры.
    """

    def __init__(self, name: str, is_dir: bool = True):
        """
        :param name: Имя узла.
        :param is_dir: Флаг, указывающий, является ли узел директорией.
        """
        self.name = name
        self.is_dir = is_dir
        self.children: List[Node] = []

    def add_child(self, child: 'Node'):
        """
        Добавляет дочерний узел.

        :param child: Дочерний узел для добавления.
        """
        self.children.append(child)


def build_tree() -> Node:
    """
    Строит дерево файловой структуры и возвращает корневой узел.

    :return: Корневой узел дерева файловой структуры.
    """
    data = Node('tree_class', is_dir=True)

    structure: List[dict] = [
        {
            'name': 'Папка А',
            'is_dir': True,
            'child': [
                {
                    'name': 'Папка В',
                    'is_dir': True,
                    'child': []
                },
                {
                    'name': 'Папка С',
                    'is_dir': True,
                    'child': [
                        {'name': 'Файл 1', 'is_dir': False, 'child': None},
                        {'name': 'Файл 2', 'is_dir': False, 'child': None},
                        {'name': 'Файл 3', 'is_dir': False, 'child': None}
                    ]
                },
                {'name': 'Файл 10', 'is_dir': False, 'child': None},
                {'name': 'Файл 11', 'is_dir': False, 'child': None},
                {'name': 'Файл 12', 'is_dir': False, 'child': None}
            ]
        },
        {'name': 'Файл 20', 'is_dir': False, 'child': None},
        {'name': 'Файл 21', 'is_dir': False, 'child': None},
        {'name': 'Файл 22', 'is_dir': False, 'child': None},
        {'name': 'Папка G', 'is_dir': True, 'child': []}
    ]

    def add_node(node, item):
        child_node = Node(item['name'], item['is_dir'])
        if item['child']:
            for child in item['child']:
                add_node(child_node, child)
        node.add_child(child_node)

    for item in structure:
        add_node(data, item)

    return data


def create_directory(root_path: str, name: str, is_dir: bool):
    """
    Создает директорию или файл в указанном пути.

    :param root_path: Путь к корневой директории.
    :param name: Имя директории или файла.
    :param is_dir: Флаг, указывающий, создавать ли директорию (True) или файл (False).
    """
    path = os.path.join(root_path, name)
    try:
        if is_dir and not os.path.exists(path):
            os.makedirs(path)
        elif not is_dir:
            file_path = path + '.txt'
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
    except OSError as e:
        logging.error(f"Error: {e}")


def create_tree(root_path: str, node: Node):
    """
    Рекурсивно создает файловую структуру, начиная с указанного узла.

    :param root_path: Путь к корневой директории.
    :param node: Корневой узел, с которого начинается создание структуры.
    """
    create_directory(root_path, node.name, node.is_dir)
    for child in node.children:
        create_tree(os.path.join(root_path, node.name), child)


def main():
    root_node = build_tree()
    root_directory = ''

    create_tree(root_directory, root_node)


if __name__ == '__main__':
    main()
