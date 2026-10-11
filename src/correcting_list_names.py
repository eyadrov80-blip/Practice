import re

# # Паттерн для ловли текста
# TEXT_PATTERN = r"[^a-zA-Zа-яА-ЯёЁ]+"
# Компилируем шаблон один раз: это эффективнее, если функция вызывается много раз
TEXT_PATTERN = re.compile(r"[^A-Za-zA-Яа-яЁё]")


def correcting_list_names(raw_list: list[str]) -> list[str]:
    '''
    Возвращает новый список с очищенными строками (Только буквы), пустые строки удаляет из списка.
    :param raw_list:
    :return:
    '''
    # correct_list = []
    # for correcting_strings in raw_list:
    #     val = re.sub(TEXT_PATTERN, '', correcting_strings)
    #     if val:
    #         correct_list.append(val)
    # return correct_list
    # fmt: off
    return [
        correct_list for correcting_strings in raw_list
        if (correct_list := TEXT_PATTERN.sub("", correcting_strings))
    ]
    # fmt: on
    # Здесь используется оператор «морж» (:=)
    # Он присваивает результат очистки переменной val и сразу проверяет, не пустая ли она.
    # Это удобно, но требует Python 3.8+.
