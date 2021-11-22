"""
6. Написати скрипт, який об'єднає три словника в самий перший. Оновлюється тільки перший словник. Дані можна "захардкодити".
        Sample Dictionary :
        dict_1 = {1:10, 2:20}
        dict_2 = {3:30, 4:40}
        dict_3 = {5:50, 6:60}
        Expected Result : dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

first_dictionary = {1: 11, 2: 22, 3: 33}
second_dictionary = {4: 44, 5: 55, 6: 66}
third_dictionary = {7: 77, 8: 88, 9: 99}

first_dictionary.update(second_dictionary)
first_dictionary.update(third_dictionary)

print(f"first_dictionary = {first_dictionary}")

