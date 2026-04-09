# To take age 
age=int(input("Enter Age:"))
# age is less than 18 then minor
if age<18:
    print("Minor")
# age is less than 65 adult
elif age<65:
    print("Adult")
# age greater than And equal to 65 Senior
else:
    print("Senior")