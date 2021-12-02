# 5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci (count):
    fib1 = fib2 = 1
    n = count - 2
    while n > 0 and fib1 < count:
        fib1 , fib2 = fib2 , fib1 + fib2
        if (fib1 < count):
            print(f"{fib1}\n")
        n -= 1
        
n = int(input("Введіть число Фібоначчі: "))
fibonacci (n)
