#  4. Write a script to concatenate N strings.


user_number =int(input('Введіть кількість строк які хочете додати:'))

result =""
for i in range(user_number):
    print(i)
    user_input = input("Введіть строку: ")
    result+=user_input
print(result)
