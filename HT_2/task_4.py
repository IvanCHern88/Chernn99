"""
4. Написати скрипт, який об'єднає три словника в новий. Початкові словники не повинні змінитись. Дані можна "захардкодити".
        Sample Dictionary :
        dict_1 = {1:10, 2:20}
        dict_2 = {3:30, 4:40}
        dict_3 = {5:50, 6:60}
        Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

def task4(dict_a, dict_b, dict_c):
    res_dict = dict_a
    res_dict.update(dict_b)
    res_dict.update(dict_c)
    return res_dict


dict1 = {1: 10, 2: 200, 3: 210}
dict2 = {4: 30, 5: 40}
dict3 = {6: 50, 7: 60}

print(task4(dict1, dict2, dict3))
