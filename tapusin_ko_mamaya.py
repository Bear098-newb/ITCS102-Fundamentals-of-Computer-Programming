for x in range(5,0,-1):
    for y in range(x):
        print("-",end=" ")
    for z in range(1,7-x):
        print(z,end=" ")
    for a in range(1,5):
        for b in range(a):
            print(a,end=" ")
    print()
