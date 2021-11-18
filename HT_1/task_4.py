#  4. Write a script to concatenate N strings.


user_number = int(input('Введіть кількість строк які хочете додати:'))

result = ""
strs = list(input('Введіть строки через кому:').split(','))
for curr in strs:
    result = result + curr

print(result)
