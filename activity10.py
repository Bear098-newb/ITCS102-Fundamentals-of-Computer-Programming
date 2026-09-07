#activity 10 if else function

username = "user1"
password = "pogi123"

user = input("input username: ")
pas = input("input password: ")

if user == username and pas == password:
    result = "correct user and password"
else:
    result = "access denied. try again."

print(result)