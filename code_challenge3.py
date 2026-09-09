#code challenge 3 LBC

name = input("sender name: ")
item_type = input("type of item: ")
fragile = input("fragile? (y/n): ")
print()
print("other information")
weight = float(input("weight{kg}"))
distance = float(input("distance{km}"))
express = input("express? (y/n): ")
international = input("international? (y/n): ")

base_cost = (weight*2.50)+(distance*0.15)
total = base_cost

if weight <= 2 or distance <= 100:
    add = 0.00
elif (express == "y" or express == "yes") and (international == "y" or international == "yes"):
    add = (total * 1.40)+50
elif express =="y" or express == "yes" or international == "y" or international == "yes":
    add = (total*1.20)+25
elif weight > 30 or distance > 1000:
    add = total + 30
elif express == "n" or express == "no" and international == "n" or international == "no":
    add = total
else :
    print("error")

print()
print("===========order overview==========")
print("name of sender:",name, "\n type of item:", item_type)
print("total cost: PHP",add)
