import getpass

username = "aj"
password = "pogi123"
print("Log In")
user_login = input("user name: ")
user_password = getpass.getpass("password: ")
 
if user_login == username and user_password == password:
    print("\nloading \n")
else:
    print("wrong username and password.")
    exit()
print("personal information:")
name = input("enter Full Name: ")
age = eval(input("enter age: "))
is_employed = bool(input("are you employed (yes/no): ") == "yes")
job = input("what is your job: ")
annual_income = eval(input("annual income: "))
credit_score = eval(input("credit_score: "))
has_collateral = bool(input("do you have collateral(yes/no): ") == "yes" )
typee = input("whats your collateral (land, vehicle, jewelry, etc..): ")
value = eval(input("value your collateral: "))
loan = eval(input("how much is your loan:PHP  "))

if has_collateral == True:
    if value >= 30000:
        print("collateral Valid")
    else:
        print("collateral Invalid")
        exit()
else:
    print("no collateral")

if is_employed == True and age >= 21 and age <= 65:
    if credit_score >= 750:
        if annual_income >= 100000:
            product = 4.5
        else:
            product = 5.0
    elif credit_score >= 600 and credit_score < 750:
        if annual_income <= 40000:
            product = 9.5
        elif has_collateral == True:
            product = 7.0
        else :
            product = 8.0
    else:
        product = "rejected: credit score too low"
else:
    product = "DENIED: failed baseline criteria"

Interest = loan/product
total = Interest+loan
    
print("\noverview:\n")
print("name:", name ,"\nage:", age, "\nJob:", job, "\ncollateral:", typee, "\ninterest rate:",product,"%","\nloan:PHP", loan, "\ninterest:",Interest,"\n\ntotal:PHP",total)
