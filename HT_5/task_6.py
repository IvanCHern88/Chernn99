"""
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
"""

def myrange(*args):
    if len(args) == 1:
        return myrange1(*args)
    return myrange2_3(*args)

def myrange1(end):
    return myrange2_3(0,end)

def myrange2_3(start,end,step=1):
    start -= step
    while True:
        if start > end and step < 0:
            if (start + step <= end):
                break
        else:
            if (start + step >= end):
                break
        start += step
        yield round(start, 2)

print(*myrange(3,14))
print(*myrange(3,-5,-2))
print(*myrange(5))
