4. Write a script to concatenate N strings.


a=input('Введіть послідовність строк через кому без відступу:').split(',')
sum=''
for i in a:
    sum+=i
print(sum)
