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
    # print(BASE_DIR)
    data_dir = BASE_DIR.parent / "data"
    if not data_dir.exists():
        raise FileNotFoundError("Директория отсутствует")
    data_file = data_dir / "names.txt"
    print(data_file)
    if not data_file.exists():
        raise FileNotFoundError("Файл не найден")
    return data_file.read_text(encoding="utf-8").splitlines()


def write_file(name_file: str, list_to_file: list[str]) -> None:
    '''
    Создаёт файл в папке data и сохраняет в нём список
    :param name_file: Имя файла
    :param list_to_file: Список
    :return:
    '''
    # print(BASE_DIR)
    data_dir = BASE_DIR.parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)  # создаёт папку, если нет
    # print(data_dir)
    data_file = data_dir / name_file
    print(data_file)
    with open(data_file, 'a', encoding="utf-8") as file:
        for inx in list_to_file:
            file.write(f'{inx}\n')
    return


# Пример использования
if __name__ == "__main__":
    names = read_file()
    print(names)

    write_file('correct_list_names.txt', correcting_list_names(names))
    print(correcting_list_names(names))

    write_file('RU_names.txt', list_RU_names(names))
    print(list_RU_names(names))

    write_file('EN_names.txt', list_EN_names(names))
    print(list_EN_names(names))
