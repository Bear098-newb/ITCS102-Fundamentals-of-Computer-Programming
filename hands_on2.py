#account_holder = input("name: ")
c_age = int(input("age: "))
cubic_meters = float(input("water consumed in cubic meters: "))
is_student = input("student housing?: ") == "True"
is_industrial = input("industrial building?:") == "True"
is_peak_season = input("peak season?: ") == "True"

base_fee = 0.0
if not is_industrial:
    print("residential")
    if cubic_meters <= 20:
        base_fee = cubic_meters*12
        print(base_fee)
    elif cubic_meters <= 50:
        f20 = 240
        cubic_meters -= 20
        base_fee = cubic_meters * 18
        base_fee += f20
        cubic_meters += 20
        print("cubic:",cubic_meters)
        print(base_fee)
    else:
        f20 = 240
        n30 = 540
        cubic_meters -= 50
        base_fee = cubic_meters * 28
        base_fee += f20 + n30
        cubic_meters += 50
        print(cubic_meters)
        print(base_fee)

    if c_age >= 60 or is_student and cubic_meters <= 30:
        base_fee*=0.88
        print(base_fee)
        print("curect")
    elif cubic_meters >= 60:
        base_fee+=200
        print(base_fee)
    else:
        pass

elif is_industrial:
    print("industrial")
    if cubic_meters >= 100:
        base_fee = cubic_meters*25
        print(base_fee)
    else:
        f100 = 2500
        cubic_meters-=100
        base_fee = cubic_meters*38
        base_fee+=f100
        cubic_meters +=100
        print(cubic_meters)
        print(base_fee)

    if is_peak_season and cubic_meters > 100:
        base_fee *=1.15
        print(base_fee)
    else:
        pass
base_fee = base_fee   
if cubic_meters%10 != 0:
    base_fee += 30
else:
    pass

subtotal = base_fee
total = subtotal*1.12
print("=========overview===================")
print("subtotal:",subtotal,"\ntotal:",total)
