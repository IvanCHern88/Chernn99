"""
1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
      .......
"""

import time

print("автомобильный" + "\t" + "пешеходный")
while True:  # бесконечный цикл
    print("red" + "\t" + "green")
    time.sleep(1)  # ждешь секунду
    print("red" + "\t" + "green")
    time.sleep(1)
    print("red" + "\t" + "green")
    time.sleep(1)
    print("yellow" + "\t" + "green")
    time.sleep(1)
    print("yellow" + "\t" + "green")
    time.sleep(1)
    print("green" + "\t" + "Red")
    time.sleep(1)
    print("green" + "\t" + "Red")
    time.sleep(1)
    print("green" + "\t" + "Red")
    time.sleep(1)
    print("green" + "\t" + "Red")
    time.sleep(1)
    print("yellow" + "\t" + "Red")
    time.sleep(1)
    print("yellow" + "\t" + "Red")
    time.sleep(1)
