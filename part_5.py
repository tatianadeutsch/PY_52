"""
Часть 5. Словари
"""


"""
1. Создайте словарь содержащий данные о человеке. 
В качестве строковых ключей используйте 
его имя, возраст, пол, рост, вес, размер ноги.
"""

dict_data_person = {
    "name": "Anna",
    "age": "35",
    "gender": "f",
    "height": 170,
    "weight": 55,
}


"""
2. Выведите на экран все данные о человеке по ключам. 
"""

for key, value in dict_data_person.items():
    print(f'{key}: {value}')


"""
3. Добавьте в словарь ключ и значение размера ноги.
"""

dict_data_person["foot size"] = 38
print(dict_data_person)


"""
4. Удалите из словаря возраст.
"""

dict_data_person.pop("age")
print(dict_data_person)