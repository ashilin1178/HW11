from __future__ import annotations

from requests import get
from flask import json


# noinspection PyShadowingNames
def load_candidates_from_json(file_adress: str):
    """
    функция загружает данные из файла, расположенного по адресу в список
    """
    file = get(file_adress)
    candidates = json.loads(file.text)

    return candidates


def get_candidate(candidates, id) -> list[dict] | None:
    """
    возвращает кандидата по
    :param candidates:
    :param id:
    :return:
    """

    for candidat in candidates:
        if id == candidat["id"]:
            result = [candidat]
            return result
        else:
            return None


def get_candidate_by_name(candidates, candidat_name) -> dict | None:
    """
    возвращает кандидата по
    :param candidates:
    :param candidat_name:
    :return:
    """

    for candidat in candidates:
        if candidat_name.lower() == candidat["name"].lower():
            return candidat
        else:
            return None


def get_candidate_by_skill(candidates: list[dict], skill_name: str) -> list[dict]:
    """
    функция возвращает кандидатов по заданному навыку
    :param candidates:
    :param skill_name:
    :return:
    """
    result = []

    for candidat in candidates:
        # убираем пробелы и преобразуем строку с навыками в список
        skill = candidat['skills'].lower().replace(' ', '').split(",")
        # подготавливаем запрос по скилам для условия, убираем пробелы и переводим в нижний регистр
        skill_name_for_if = skill_name.replace(' ', '').lower()

        if skill_name_for_if in skill:
            result.append(candidat)

    return result


# adress = "https://jsonkeeper.com/b/89KW"
# #
# candidates = load_candidates_from_json(adress)
#
# print(candidates)
#
# print(get_candidate_by_name(candidates, 'adela hendricks'))
