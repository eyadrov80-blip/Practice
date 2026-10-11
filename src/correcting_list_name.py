import re

# Паттерн для ловли текста
TEXT_PATTERN = r"[^a-zA-Zа-яА-Я]+"


def correcting_list_name(raw_list: list[str]) -> list[str]:
    '''
    Возвращает новый список с очищенными строками (Только буквы), пустые строки удаляет из списка.
    :param raw_list:
    :return:
    '''
    correct_list = []
    for correcting_strings in raw_list:
        val = re.sub(TEXT_PATTERN, '', correcting_strings)
        if val:
            correct_list.append(val)
    return correct_list
