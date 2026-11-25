from acitivity23 import factorial
from acitivity23 import greet
from acitivity23 import box

while True:
    print("choose an action \n[1]factorial \n[2]greetings \n[3]box \n[4]system exit \n===============")
    choice = int(input("your choice ---> "))

    if choice == 1:
        factorial_number = int(input("Enter a number for factorial: "))
        print(acitivity23.factorial(factorial_number))
        continue

    elif choice == 2:
        name = input("whats your name --> ")
        print(greet(name))
        continue

    elif choice == 3:
        box_size = int(input("Enter box size: "))
        box(box_size)
        continue

    elif choice == 4:
        print("system exit")
        break

    else:
        print("invalid choice")
        continue
