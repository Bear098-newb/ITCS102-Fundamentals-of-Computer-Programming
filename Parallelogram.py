size = 7
for x in range(size):
    for y in range(size):
        if x == 0 and y > 1 and y<=6 or x ==1 and y ==1 or x ==1 and y ==5 or x ==2 and y<5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
