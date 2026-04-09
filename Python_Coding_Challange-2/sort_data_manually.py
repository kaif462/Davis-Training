n=int(input("Enter range:"))
lst=[]
print("enter no :")
for i in range(n):
    lst.append(int(input()))
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
print(lst)