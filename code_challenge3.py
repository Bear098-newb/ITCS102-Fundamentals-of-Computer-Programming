print("======LBC=======")
name = input("name: ")
item_type = input("item type: ")
fragile = input("is the item fragile?: ") 
IsFragile = fragile in ["y", "yes"]

print("\n=====other information======")

weight = float(input("weight in kg: "))
distance = float(input("distance in km: "))
express = input("is this express delivery?: ")
isExpress = express in ["y", "yes"]
international = input("is delivery from international: ")
isInternational = international in ["y","yes"]
base_cost = (weight*2.50)+(distance*0.15)
total = base_cost

if weight <= 2 or distance <= 99:
    add = 0.00, "free shipping"
elif isExpress and isInternational:
    add = (total*1.40)+50
elif isExpress or isInternational:
    add = (total*1.20)+25
elif weight >= 30 or distance >= 1000:
    add = total + 30
else:
    add = total

print()
print("----overall review-----")
print("sender:",name,"\nitem type: ",item_type,"\nDelivery fee: PHP", add)
