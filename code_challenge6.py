size = 5

for row in range(size):
    for column in range(size):
        if column == row or column == size - row - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
