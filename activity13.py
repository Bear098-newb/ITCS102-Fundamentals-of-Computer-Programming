age = eval(input("what is your age: "))
is_employed = bool(input("are you employed (y/n): "))
credit_score = eval(input("what is your credit score: "))
annual_income = eval(input("what is your yearly income: "))
has_collateral = bool(input("do you have a colateral? (y/n): "))


if age >= 21 and is_employed == True:
    if credit_score >= 750:
        if annual_income >= 100000:
            product = "APPROVED at 4.5% interest"
        else:
            product = "APPROVED at 5.0% interest"
    elif credit_score > 600 and credit_score < 750:
        if annual_income <= 40000:
            product = "APPROVED at 9.5% interest"
        elif has_collateral == True:
            product = "APPROVED at 7.0% interest"
        else :
            product = "APPROVED at 8.0% interest"
    else:
        product = "rejected: credit score too low"
else:
    product = "DENIED: failed baseline criteria"
print(product)
