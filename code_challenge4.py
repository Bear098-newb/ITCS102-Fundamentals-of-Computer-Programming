print("create an account to continue.")
name = input("create a username: ")
passwrd = input("create a password: ")
print()
print("Log in")
logname = input("username: ")
logpasswrd = input("password: ")
print()
if logname == name and logpasswrd == passwrd:
    print("continue")
else:
    print("wrong credentials try again.")
    exit()
print()
name = input("what is your full name: ")
age = eval(input("what is your age: "))
is_employed = bool(input("are you employed (y/n): ") == "y")
job = input("tell me about your job description: ")
credit_score = eval(input("what is your credit score: "))
annual_income = eval(input("what is your yearly income: "))
has_collateral = bool(input("do you have a colateral? (y/n): ") == "y")
print()
loan = eval(input("how much do you want to loan: "))


if has_collateral == True:
    collateral = input("describe your collateral (motorcycle, land etc): ")
    value = eval(input("what is the value of your collateral: "))
    if value >= 30000:
        print("loading")
    else:
        print("value less than 30k. invalid")
else:
    print("no collateral.")

if is_employed == True and age >= 21 and age <= 65:
    if credit_score >= 750:
        if annual_income >= 100000:
            product = "APPROVED at 4.5% interest"
        else:
            product = "APPROVED at 5.0% interest"
    elif credit_score >= 600 and credit_score < 750:
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

Interest = loan/product
total = Interest+product
print()
print(name,)