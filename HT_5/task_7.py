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

  for n in iterableSeq:
    if n == iterableSeq[-1]:
      yield n
      for elem in MyGenerator(iterableSeq):
        print(elem)
    else:
      yield n


if __name__ == "__main__":
  for elem in MyGenerator([1, 2, 3]): 
    print(elem)

