import json
from diarybook import Diary


def read_from_json_into_app(path):
    with open(path) as file:
        data = json.load(file)
        diaries = []
        for entry in data:
            diaries.append(Diary(entry["memo"], entry["tags"]))
        return diaries
