n=int(input("Enter range:"))
lst=[]
print("enter lst :")
for i in range(n):
    lst.append(int(input()))
t=tuple(lst)
print(t)