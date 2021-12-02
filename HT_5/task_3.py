"""
3. На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
   """

class PasswordException(Exception):
	def __init__(self, message):            
		super().__init__(message)

class User():

	login = ""
	password = ""
	def __init__(self, login, password):
		self.login = login
		self.password = password

def ValidateAuth(login, password):
          if len(login) < 3 or len(login) > 50:
                raise LoginException("Incorrect login size! Login should minimal contain 3 symbols and maximum is 50 symbols!")
          if len(password) < 8:
                raise PasswordException("Incorrect password size! Password should contain 8 symbols or more!")
          if re.search('\d+', password) is None:
                raise PasswordException("Incorrect password! Password should contain digits!")
          if not "." in password:
                raise PasswordException("Incorrect password! Password should contain one more DOT!")
if __name__ == "__main__":
	users = [
			User("t", "testpassword"),
			User("somelogin", "qwerty12345"),
			User("helloworld123", "mypa.ss1337"),
			User("12345", "ls12345"),
			User("Mike1991", "m.ike1991")
			]
	for user in users:
		print("Name: %s\nPassword: %s" % (user.login, user.password))
		try:
			ValidateAuth(user.login, user.password)
			print("Status: OK!")
		except LoginException:
			print("Status: Login entering error!")
		except PasswordException:
			print("Status: Password entering error")
		finally:
			print("\n")




