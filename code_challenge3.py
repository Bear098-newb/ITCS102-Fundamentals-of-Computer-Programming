print("======LBC=======")
name = input("name: ")
item_type = input("item type: ")
fragile = bool(input("is the item fragile? (y/n): ") == "y")


print("\n=====other information======")

weight = float(input("weight in kg: "))
distance = float(input("distance in km: "))
express = bool(input("is this express delivery? (y/n): ") == "y") 
international = bool(input("is delivery from international? (y/n): ") == "y") 
base_cost = (weight*2.50)+(distance*0.15)
total = base_cost
isInternational = True
isExpress = True


if weight <= 2 or distance <= 99:
    add = 0.00 , "FREE SHIPPING"
elif express == True and international == True:
    add = (total*1.40)+50
elif express == True or international == True: 
    add = (total*1.20)+25
elif weight >= 30 or distance >= 1000:
    add = total + 30
else:
    add = total

print()
print("----overall review-----")
print()
print("sender:",name,"\nitem type: ",item_type,"\nexpress:",express,"\ninternational:",international,"\nfragile: ", fragile,"\nbase cost : PHP",total,"\ntotal cost: PHP", add)
print("-----end of review-----")
