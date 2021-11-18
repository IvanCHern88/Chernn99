"""
6. Write a script to check whether a specified value is contained in a group of values.
        Test Data :
        3 -> [1, 5, 8, 3] : True
        -1 -> (1, 5, 8, 3) : False
"""
          
print('Введіть числа в список через кому без відступу:')
a=input().split(',') # створює список строк 
for i in range(len(a)):
    a[i]=int(a[i])
b=int(input('Введіть число яке хочете перевірити у списку: '))    
print(b,"-->",a,b in a,":",sep=' ')
