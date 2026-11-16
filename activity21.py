passenger = ["ana", "ben", "carla"]
passenger.append("dan")
print(passenger)
passenger.insert(0,"lola")
print(passenger)
passenger.remove("ben")#ben bumaba
print(passenger)
y = passenger.pop()
print(passenger)
x = passenger.pop(0)
print(passenger)
check = len(passenger)
onboard = "ana" in passenger
print(check)
print(onboard)
passenger.reverse()
print(passenger)

route = ["Terminal", "Perez Park", "Pacific Mall"]
passengers = []
seats = 6
fare = 13
total = 0

while True:
    print()
    print("sakay: ",passengers)
    print(len(passengers), "of", seats, "seats")
    print("1 sakay 2 Priority seat 3 Para po!")
    print("4 baba sa likod 5 baba sa harap")
    print("6 seat check 7 balikan 8 Exit")
    choice = input("choice: ")

    if choice == "1":
        if len(passengers) == seats:
            print("puno na!")
        else:
            name = input("name: ")
            passengers.append(name)
            total = total + fare
            print(name, "sumakay sa likod")
        
    elif choice == "2":
        if len(passengers) == seats:
            print("puno na!")
        else:
            name = input("name: ")
            passengers.insert(0,name)
            total = total + fare
            print(name, " took the Priority seat")
    
    elif choice == "3":
        name = input("who got off: ")
        if name in passengers:
            passengers.remove(name)
            print(name, "got off, ingat love you")
        else:
            print(name, "is not on this jeep.")

    elif choice == "4":
        if len(passengers) == 0:
            print("wala na tao buseng")
        else:
            left = passengers.pop()
            print(left, "bumaba buseng")

    elif choice == "5":
        if len(passengers) == 0:
            print("walang tao nganiii")
        else:
            front = passengers.pop(0)
            print(front, "bumaba sa harap")

    elif choice == "6":
        for i in range(len(passengers)):
            print("seat", i + 1, passengers[i])

    elif choice == "7":
        route.reverse()
        print("route: ", total)
        
    elif choice == "8":
        print("total fare ngayon: ", total)
        break

    else:
        print("invalid choice")
