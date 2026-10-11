import re

# Компилируем шаблон один раз: это эффективнее, если функция вызывается много раз
RUS_PATTERN = re.compile(r"[^А-Яа-яЁё]")
ENG_PATTERN = re.compile(r"[^A-Za-z]")


def list_RU_names(raw_list: list[str]) -> list[str]:
    '''
    Возвращает сортированный список строк на кириллице
    :param raw_list:
    :return:
    '''
    # fmt: off
    return sorted([
        correct_list
        for correcting_strings in raw_list
        if (correct_list := RUS_PATTERN.sub("", correcting_strings))
    ])
    # fmt: on


def list_EN_names(raw_list: list[str]) -> list[str]:
    '''
    Возвращает сортированный список строк на латинице
    :param raw_list:
    :return:
    '''
    # fmt: off
    return sorted([
        correct_list
        for correcting_strings in raw_list
        if (correct_list := ENG_PATTERN.sub("", correcting_strings))
    ])
    # fmt: on
