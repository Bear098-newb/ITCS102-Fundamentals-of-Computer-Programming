#activity 12

name = input("name: ")
age = int(input("age: "))

if age >= 0 and age <= 5 :
    result = "you are an INFANT"
elif age >= 6 and age <= 12 :
    result = "you are a KID"
elif age >= 13 and age <= 15 :
    result = "you are a PRE TEEN"
elif age >= 16 and age <= 18 :
    result = "you are a TEENAGER"
elif age >= 19 and age <= 29 :
    result = "you are in EARLY ADULTHOOD"
elif age >= 30 and age <= 58 :
    result = "you are  an ADULT"
elif age >= 59 and age <= 150 :
    result = "you are a SENIOR"
else :
    result = "ivalid. OVERAGE!!!"

print(result)