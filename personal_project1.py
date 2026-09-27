#personal project 1
print("shop products: \nbag:₱400 \nbasketball(on-sale):₱1000 \nvolleyball (on-sale):₱289 \nfootball:₱399")
print("\n")
name = input("name of buyer:")
age = int(input("age:"))
if age >= 18:
    print()
else:
    print("underage:")
    exit()
item_name = input("item to purchase:")
quantity = int(input("quantity:"))
if item_name == "bag":
    price = 400
elif item_name == "basketball":
    price = 1000
elif item_name == "volleyball":
    price = 289
elif item_name == "football":
    price = 399
else:
    print("check spelling or item not a product. kindly start over.")
    exit()
print("item price:₱",price)
is_member = input("are you a member(yes/no): ")
is_onsale = input("is the item on sale(yes/no): ")
distance = int(input("distance in kilometers: "))

sub_total = price*quantity

if is_onsale == "yes":
    if sub_total >= 5000:
        discount = 0.15
    elif sub_total < 5000 and sub_total > 2000:
        discount = 0.10
    else:
        discount = 0.05
else:
    discount = 0

sub_total1 = sub_total*discount
sub_total2 = sub_total-sub_total1

if is_member == "yes":
    if sub_total2 >= 3000:
        member_discount = 0.05
    else:
        member_discount = 0
else:
    member_discount = 0

if distance <= 10:
    d_fee = 50
elif distance <= 30:
    d_fee = 100
elif distance <= 50:
    d_fee = 150
else:
    d_fee = 250
mem_discount = sub_total2*member_discount
total = sub_total-sub_total1-mem_discount+d_fee

print("\n=========ORDER SUMMARY=============")
print("\n")
print("name:",name,"\nitem:",item_name, "\nquantity:",quantity)
print("subtotal:₱",sub_total,"\non sale discount:₱",sub_total1,"\nmembership discount:₱",mem_discount,"\ndelivery fee:₱",d_fee,"\ntotal:₱",total )
