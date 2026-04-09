str=input("Enter Sting:")
count=0
for c in str:
    if c in 'aeiou':
        count+=1
print(count)