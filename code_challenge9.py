amount = int(input("loan amount: "))
years = int(input("how many years do you intend to pay: "))

months = years * 12
principal = amount / months
remaining_loan = amount
interest_rate = 0.0025
interest = amount*interest_rate

print("Month | Monthly payment | Interest | Principal | Remaining loan")
print("-" * 69)

for x in range(1, months + 1):
    interest = remaining_loan * interest_rate
    monthly_payment = principal + interest
    remaining_loan -= principal
    print(x, "\t\t", round(monthly_payment, 2),"\t\t\t", round(interest, 2),
         "\t\t", round(principal, 2),"\t\t", round(remaining_loan, 2))

height = 6
base_width = 12

for x in range(height):
    if x == height - 1:
        print("*" * base_width)
    elif x == 0:
        print(" " * (height - 1) + "*")
    else:
        print(" " * (height - x - 1) + "*" + " " * (2 * x - 1) + "*")

size = 5
for x in range(size):
    for y in range(size):
        if x == 0 or x == size - 1 or y == size - 1 - x:
            print("*", end="")
        else:
            print(" ", end="")
    print()
