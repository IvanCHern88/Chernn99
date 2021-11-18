# 5. Write a script to convert decimal to hexadecimal
        Sample decimal number: 30, 4
        Expected output: 1e, 04
        
        
a=input('Введіть Послідовність чисел через кому без відступу: ').split(',')
for i in range(len(a)):
    a[i]=int(a[i])
    a[i]=hex(a[i])
print("Результат: ",*a,sep=",")

