print("======LBC=======")
name = input("name: ")
item_type = input("item type: ")
fragile = bool(input("is the item fragile? True or False: "))


print("\n=====other information======")

weight = float(input("weight in kg: "))
distance = float(input("distance in km: "))
isExpress = bool(input("is this express delivery? True or False: "))
#isExpress = express in ["y", "yes"]
isInternational = bool(input("is delivery from international? True or False: "))
#isInternational = international in ["y","yes"]
base_cost = (weight*2.50)+(distance*0.15)
total = base_cost

if weight <= 2 or distance <= 99:
    add = 0.00, "free shipping"
elif isExpress == True and isInternational == True:
    add = (total*1.40)+50
elif isExpress == True or isInternational == True:
    add = (total*1.20)+25
elif weight >= 30 or distance >= 1000:
    add = total + 30
else:
    add = total

print()
print("----overall review-----")
print("base cost : PHP",total)
print("sender:",name,"\nitem type: ",item_type,"\ntotal cost: PHP", add)
print()
print("if the outcome is same please use True or False with a uppercase letter on ONLY the first letter")
