# -*- coding: utf-8 -*-

from enum import Enum

token = '' # Вставить сюда токен бота
db_file = "database.vdb"


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_DAY = "1"
    S_COUNTRY_OR_REGION = "2"
    S_ENTER_COUNTRY_OR_REGION = "3"
    S_ENTER_FIELD_LIST = "4"
