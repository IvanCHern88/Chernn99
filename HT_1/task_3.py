# 3. Write a script to sum of the first n positive integers.

print("Введіть числа через кому без відступу:")
a=input().split(',')
sum=0
for i in a:
    i=int(i)
    if i>0:
        sum+=i
print(sum)
