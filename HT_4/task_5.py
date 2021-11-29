# 5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci (count):
    if count == 1 :
        print('-')
    fib1 = 1
    fib2 = 1
    sum = 2
    i = 0
    while fib2 != count:
        sum_fib12 = fib1 + fib2
        fib1 = fib2
        fib2 = sum_fib12
        sum += fib2
        i += 1
        print(fib2)



n = int(input("Введіть число Фібоначчі: "))
fibonacci (n)
