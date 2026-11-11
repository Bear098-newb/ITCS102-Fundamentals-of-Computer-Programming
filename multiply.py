columns = int(input("#L: "))
rows = 11
for x in range(1,rows):
    for y in range(1,columns+1):
        print(x,"x",y,"=",x*y,"\t", end = " ")
    print()
