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