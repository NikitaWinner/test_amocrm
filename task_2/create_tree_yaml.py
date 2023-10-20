import yaml
import logging
from pathlib import Path
from typing import Optional


logging.basicConfig(
    filename='tree_yaml.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    encoding='utf-8'
)


def load_yaml_file(yaml_file_path: str) -> Optional[dict]:
    """
    Загружает структуру из YAML файла.

    :param yaml_file_path: Путь к YAML файлу.
    :return: Загруженная структура в формате словаря или None в случае ошибки.
    """
    try:
        with open(yaml_file_path, 'r', encoding='utf-8') as yaml_file:
            return yaml.load(yaml_file, Loader=yaml.FullLoader)
    except (yaml.YAMLError, FileNotFoundError) as e:
        logging.error(f"Ошибка при загрузке YAML файла: {e}")
        return None


def create_tree(base_path: Path, structure: dict) -> None:
    """
    Рекурсивно создает структуру директорий и файлов на основе переданной структуры.

    :param base_path: Базовый путь для создания структуры (тип Path).
    :param structure: Структура данных, описывающая директории и файлы.
    """
    project_name = structure.get('project_name')
    if project_name:
        base_path /= project_name
        base_path.mkdir(parents=True, exist_ok=True)

    for file in structure.get('files', []):
        file_name = file['name']
        file_content = file.get('content', '')

        file_path = base_path / file_name
        with file_path.open('w', encoding='utf-8') as f:
            f.write(file_content)

    for folder in structure.get('folders', []):
        folder_name = folder['name']
        folder_path = base_path / folder_name
        folder_path.mkdir(parents=True, exist_ok=True)
        create_tree(folder_path, folder)


def main() -> None:
    """
    Основная функция для выполнения создания
    директорий и файлов на основе YAML-структуры.
    """
    yaml_file_path = 'structure.yaml'
    base_path = Path('')  # базовый путь

    if not Path(yaml_file_path).is_file():
        logging.error(f"Файл {yaml_file_path} не найден.")
        return

    structure = load_yaml_file(yaml_file_path)
    if structure is None:
        return

    create_tree(base_path, structure)
    logging.info("Структура успешно создана.")


if __name__ == "__main__":
    main()
