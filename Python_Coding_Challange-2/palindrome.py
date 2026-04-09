n=int(input("Enter No:"))
orig=n
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
if orig==rev: print('Palindrome')
else: print('Not Palindrome')