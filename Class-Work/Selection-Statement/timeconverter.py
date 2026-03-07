#program to input time in seconds and convert it into hours,minutes and seconds
#taking input from user
second=int(input("Enter time in seconds: "))
hours=0
minutes=0
# calucalting hours 
if second>=3600:
    hours=second//3600
    second=second%3600
    # calucalting minutes 
if second>=60:
    minutes=second//60
    second=second%60
print("Time:",hours,"hrs",minutes,"min",second,"seconds")