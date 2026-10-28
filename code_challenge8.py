for x in range(7):
    for y in range(7):
        if x + y == 3 or y-x == 3 or x-y==3 or y+x==9 or x**y==81 or y**x==81 or y**x==8 or y**x==9:
            print("x", end=" ")
        else:
            print(" ",  end=" ")
    print()
