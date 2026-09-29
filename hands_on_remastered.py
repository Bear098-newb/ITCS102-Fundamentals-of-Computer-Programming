owner_age = int(input("age: "))
revenue = int(input("monthly revenue:₱ "))
credit_score = int(input("what is your credit score: "))
years_in_business = float(input("years in business: "))
has_defaults = input("have you ever filed for bankruptcy: ")
collateral = input("what's your colateral: ")
c_value = int(input("value your collateral:₱ "))
loan = int(input("how much do you want to loan: ₱"))

max_loan = 0
base_fee = 0.0
if owner_age >= 21 and years_in_business >= 2 and has_defaults == "no":


    if credit_score >= 720:#tier 1
        max_loan = revenue*3
        base_fee = 0.0
        if revenue >= 50000:
            interest = 0.015
            base_fee = max_loan*interest
            print("base fee = ₱",base_fee)
        else:
            interest = 0.025
            base_fee = max_loan*interest
            print("base fee = ₱",base_fee)
    
        if c_value >= max_loan:
            print("collateral accepted.")
        else:
            print("REJECTED:collateral value too low")
            exit()
    elif credit_score >= 620 and credit_score < 720:#tier2
        max_loan = revenue* 1.5
        base_fee = 0.0
        if years_in_business >= 5:
            interest = 0.02
            base_fee = max_loan*interest
            print("base fee = ₱",base_fee)
        else:
            interest = 0.035       
            base_fee = max_loan*interest
            print("base fee = ₱",base_fee)  

        if c_value >= max_loan:
            print("collateral accepted.")
        else:
            print("REJECTED:collateral value too low")
            exit()
    else: #tier3
        print("REJECTED: credit score too low")
        exit()
else:
    print("REJECTED: failed bseline requirement")
    exit()

surcharge = max_loan*base_fee %5000
if surcharge != 0:
    base_fee = base_fee + 250
else:
    base_fee = base_fee
print("\n============OVERVIEW===========")
print( "collateral: ",collateral, "\nmax loan: ₱",max_loan ,"\nloan: ₱",loan, "\nbase fee: ₱", base_fee)
