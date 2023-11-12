import json

def task() -> float:
    file = "input.json"
    with open(file, encoding='utf-8') as read_file:
        json_data = json.load(read_file)

    res_value = sum([item["score"] * item["weight"] for item in json_data])
    return round(res_value, 3)

print(task())
