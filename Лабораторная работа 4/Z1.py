# TODO решите задачу
import json

filename = "input.json"


def task() -> float:
    with open(filename) as f:  # Открываем и читаем JSON файл
        json_data = json.load(f)
        sum_of_products = sum(dict['score'] * dict['weight'] for dict in json_data)    # Вычисляем сумму произведений
    return round(sum_of_products, 3)  # Округляем до 3 знаков после запятой и возвращаем результат


data = task()
print(data)  # Выводим результат
