for x in range(8):
    for y in range(4):
        if x == 4 or y == 4 or x == 3 and y > 0 or x == 2 and y >1 or x == 1 and y > 2 or x ==5 and y >0 or x == 6 and y>1 or x==7 and y >2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
