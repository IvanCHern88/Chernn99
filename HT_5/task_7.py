"""
7. Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) і повертає генератор, який буде вертати значення з цієї послідовності, при цьому, якщо було повернено останній елемент із послідовності - ітерація починається знову.
   Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
   >>>for elem in generator([1, 2, 3]):
   ...    print(elem)
   ...
   1
   2
   3
   1
   2
   3
   1
   .......
   """



def MyGenerator(iterableSeq):
  while True:
    for i in iterableSeq:
      if i == iterableSeq[-1]:
        yield i
        break
      yield i
    else:
      break


if __name__ == "__main__":
  for elem in MyGenerator([1, 2, 3]): 
    print(elem)
