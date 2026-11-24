# Box

def box(number):
    for x in range(number):
        for y in range(number):
            if x == 0 or y == 0 or x == number - 1 or y == number - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


box_size = int(input("Enter box size: "))
box(box_size)


# Factorial

def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    print(result)


factorial_number = int(input("Enter a number for factorial: "))
factorial(factorial_number)

#greet

def greet(yaho):
    helo = "hello " + yaho + ", pogi mo po"
    return helo

name = input("whats your name --> ")
print(greet(name))

