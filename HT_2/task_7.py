"""
7. Написати скрипт, який отримає максимальне і мінімальне значення із словника. Дані захардкодити.
                Приклад словника (можете використовувати свій):
                dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
                Вихідний результат:
                MIN: 10
                MAX: 60
                
"""

dictionary = {1 : 11, 2 : 2, 3 : 89, 4: 32, 5 : 188}

max_element = max(list(dictionary.values()))
min_element = min(list(dictionary.values()))

print(f"MAX: {max_element}")
print(f"MIN: {min_element}")


