n=int(input("Enter Range:"))

list=[]
print("Enter Numbers:")
for i in range(n):
    list.append(int(input()))
count=0
for i in list:
    if i>50:
        count+=1
print(count)