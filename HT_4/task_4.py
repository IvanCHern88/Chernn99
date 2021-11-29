#  4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.

def prime(n):
    if n < 2:
        return False
    for i in [num for num in list(range(2, n+1)) if num*num <= n]:
        if n % i == 0:
            return False
    return True


def prime_list(first, last):
    return [i for i in list(range(first, last+1)) if prime(i)]


print(prime_list(41, 97))
