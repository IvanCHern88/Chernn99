"""
2. Написати скрипт, який пройдеться по списку, який складається із кортежів, і замінить для кожного кортежа останнє значення.
   Список із кортежів можна захардкодити. Значення, на яке замінюється останній елемент кортежа вводиться користувачем.
   Значення, введене користувачем, можна ніяк не конвертувати (залишити рядком). Кількість елементів в кортежу повинна бути різна.
             Приклад списка котежів: [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
             Очікуваний результат, якщо введено "100":
        Expected Output: [(10, 20, "100"), (40, 50, 60, "100"), (80, "100"), ("100",)]
"""

def task2(a_list):
    value = input("Введіть значення: ")
    a_list = [() if len(item) == 0 else (value,) if len(item) == 1 else (*item[:-1], value) for item in a_list]
    return a_list


print(task2([(1, 2, 4), (35, 100, 456, 88), ('122', 1), ('22', 23), (23,), ()]))
