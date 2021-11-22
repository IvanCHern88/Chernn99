"""
3. Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
        Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
"""

def task3(a_list):
    return [item for item in a_list if len(item) > 0]


print(task3([{}, '',  {'e': 13, 32: 'er'}, [34, "rer"], [], (1, 2), ()]))
