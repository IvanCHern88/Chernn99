"""
5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для
   роботи захардкодити свій.
                Приклад словника (не використовувати):
                {'a': 1, 'b': 3, 'c': 1, 'd': 5}
                Очікуваний результат:
                {'a': 1, 'b': 3, 'd': 5}
"""

dictionary = {"Maxim": 11, "Rick": 12, "Justin": 11, "Andrey": 12}

values = set()
new_dictionary = {}

for k, v in dictionary.items():
    if v not in values:
        new_dictionary.update({k: v})
        values.add(v)

print(new_dictionary)
