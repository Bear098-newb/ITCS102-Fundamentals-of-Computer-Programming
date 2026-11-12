amount = int(input("loan amount: "))
years = int(input("how many years do you intend to pay: "))

months = years * 12
interest = 0.0025
principal = amount / months
remaining_loan = float(amount)
monthly_payment = principal + interest
print("Month | Monthly payment | Interest | Principal | Remaining loan")
print("-" * 69)
