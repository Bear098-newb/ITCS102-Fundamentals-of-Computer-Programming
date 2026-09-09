#code challenge 3 LBC

name = input("sender name: ")
item_type = input("type of item: ")
fragile = input("fragile? (y/n): ")
print()
print("other information")
weight = float(input("weight{kg}"))
distance = float(input("distance{km}"))
express = input("express? (y/n): ")
internaional = input("international? (y/n): ")

base_cost = (weight*2.50)+(distance*0.15)
total = base_cost

if weight <= 2 or distance <= 100:
    add = 0.00
elif (express == "y" or express == "yes") and (internaional == "y" or internaional == "yes"):
    add = (total * 1.40)+50
elif express =="y" or express == "yes" or internaional == "y" or internaional == "yes" or weight > 20:
    add = (total*1.20)+25
elif weight > 30 or distance > 1000:
    add = total + 30
elif express == "n" or "no" and internaional == "n" or internaional == "no":
    add = total
else :
    print("error")

print()
print("===========order overview==========")
print("name of sender:",name, "\n type of item:", item_type)
print("total cost: PHP",add)
