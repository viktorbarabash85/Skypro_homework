import json


def read_json_file(file_path: str) -> float:
    """Читает JSON-файл и возвращает список словарей с данными о транзакциях."""
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            repos = json.load(file)
        if isinstance(repos, list):
            return repos
        else:
            return []
    except Exception as e:
        print(f"Ошибка {e}")
        return []
