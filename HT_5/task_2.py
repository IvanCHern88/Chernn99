"""
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
"""

import re

class LoginException(Exception):
  def __init__(self, message):            
    super().__init__(message)
class PasswordException(Exception):
  def __init__(self, message):            
    super().__init__(message)


def ValidateAuth(login, password):
  if len(login) < 3 or len(login) > 50:
    raise LoginException("Incorrect login size! Login should minimal contain 3 symbols and maximum is 50 symbols!")
  if len(password) < 8:
    raise PasswordException("Incorrect password size! Password should contain 8 symbols or more!")
  if re.search('\d+', password) is None:
    raise PasswordException("Incorrect password! Password should contain digits!")


if __name__ == "__main__":
  while True:
    print("<----------START INPUTING (enter <0> - to end)---------->")
    login = input("[INPUTING] Enter login: ")
    if login == "0":
      break
    password = input("[INPUTING] Enter password: ")
    if password == "0":
      break

    ValidateAuth(login, password)
    print("\n[RESULT] Correct!")
