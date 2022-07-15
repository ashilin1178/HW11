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


def get_candidate(candidates_, id) -> dict | None:
    """
    возвращает кандидата по
    :param candidates_:
    :param id:
    :return:
    """

    for candidat in candidates_:
        if id == candidat["id"]:
            result = candidat
            return result


def get_candidate_by_name(candidates_, candidat_name) -> list[dict] | None:
    """
    возвращает кандидата по
    :param candidates_:
    :param candidat_name:
    :return:
    """
    result = []
    for candidat in candidates_:
        if candidat_name.lower() in candidat["name"].lower():
            result.append(candidat)
    return result


def get_candidate_by_skill(candidates_: list[dict], skill_name: str) -> list[dict]:
    """
    функция возвращает кандидатов по заданному навыку
    :param candidates_:
    :param skill_name:
    :return:
    """
    result = []

    for candidat in candidates_:
        # убираем пробелы и преобразуем строку с навыками в список
        skill = candidat['skills'].lower().replace(' ', '').split(",")
        # подготавливаем запрос по скилам для условия, убираем пробелы и переводим в нижний регистр
        skill_name_for_if = skill_name.replace(' ', '').lower()

        if skill_name_for_if in skill:
            result.append(candidat)

    return result
