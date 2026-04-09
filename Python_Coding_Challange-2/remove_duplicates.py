n=int(input("Enter range:"))
lst=[]
print("enter no :")
for i in range(n):
    lst.append(int(input()))
print(list(set(lst)))