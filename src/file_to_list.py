# import os
from pathlib import Path

from src.correcting_list_names import correcting_list_names
from src.sort_list_names import list_EN_names, list_RU_names

# Путь к директории, где лежит этот файл (src/)
BASE_DIR = Path(__file__).resolve().parent
# Поднимаемся на уровень вверх к корню проекта, затем в data/
# DATA_FILE = BASE_DIR.parent / "data" / "names.txt"


def read_file() -> list[str]:
    '''
    Читаем файл с проверкой наличия директории и его наличия
    :return: Список строк
    '''
    print(BASE_DIR)
    data_dir = BASE_DIR.parent / "data"
    print(data_dir)
    if not data_dir.exists():
        raise FileNotFoundError("Директория не найда")
    data_file = data_dir / "names.txt"
    print(data_file)
    if not data_file.exists():
        raise FileNotFoundError("Файл не найден")
    return data_file.read_text(encoding="utf-8").splitlines()


# Пример использования
if __name__ == "__main__":
    names = read_file()
    print(names)
    print(correcting_list_names(names))
    print(list_RU_names(names))
    print(list_EN_names(names))

#     print(BASE_DIR)
#     print(DATA_FILE)
#     current_directory = os.getcwd()
#     print(current_directory)  # Выведет: ...\PythonProject\Practice\src
