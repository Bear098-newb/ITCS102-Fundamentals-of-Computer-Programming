from getpass import getpass
islogin = False
loginattempt = 0

us = "pogi"
ps = "pogi123"

while islogin == False:
    username = input("name: ")
    password = getpass("password: ")

    if username == us and password == ps:
        print("pogi tama password")
        print("total login attempts", loginattempt)
        islogin = True
    else:
        print("pangit, ulitin mo password")
        loginattempt += 1
        print("total login attempts", loginattempt)
        islogin = False