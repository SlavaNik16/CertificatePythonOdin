import json


def read_data_from_file():
    try:
        with open("database.txt", "r", encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except Exception:
        return []


def write_data_to_file(data):
    with open("database.txt", "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)
