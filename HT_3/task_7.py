# 7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def func(x,y,str):
   if str == '+':
       return x + y
   if str == '-':
       return x - y
   if str == '*':
       return x * y
   if str == '/' and y == 0:
       return 'Error'
   if str == '/':
       return x / y
   

print(func(4,3,'+'))
