#activity 11 if else function with getpass
import getpass

username = "user1"
password = "pogi123"

user = input("input username: ")
pas = getpass.getpass("input password: ")

if user == username and pas == password:
    result = "correct user and password"
else:
    result = "access denied. try again."

print(result)
