"""
1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException
"""

class LoginException(Exception):
  pass

class User():

  login = ""
  password = ""
  def __init__(self, login, password):
    self.login = login
    self.password = password
    
    

def CheckAuth(login, password, silent = False):
  
  users = [
      User("testlogin", "testpassword"),
      User("somelogin", "qwerty12345"),
      User("helloworld123", "mypass1337"),
      User("12345", "ls12345"),
      User("Mike1991", "mike1991")
      ]
  for user in users:
    if user.login == login and user.password == password:
      return True
  if silent:
      return False
  else:
    raise LoginException()



if __name__ == "__main__":

  while True:
    print("<----------START INPUTING (enter <0> - to end)---------->")
    login = input("[INPUTING] Enter login: ")
    if login == "0":
      break
    password = input("[INPUTING] Enter password: ")
    if password == "0":
      break
    silent = input("[INPUTING] Enter silent mode (<on> or <off>): ").lower()
    if silent == "0":
      break
    elif silent == "on":
      checkResult = CheckAuth(login, password, True)
      print("\n[CHECK RESULT] %s" % checkResult)
    else:
      checkResult = CheckAuth(login, password)
      print("\n[CHECK RESULT] %s" % checkResult)


    print("\n")
