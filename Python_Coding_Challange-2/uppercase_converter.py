str=input("Enter String")
res=''
for c in str:
    res+=chr(ord(c)-32)
print(res)