a=input("Enter the string:")
c=0
for i in range(len(a)):
    if(a[i]>='a' and a[i]<='z'):
        continue
    elif(a[i]>='A' and a[i]<='Z'):
        continue
    elif(a[i]>='0' and a[i]<='9'):
        continue
    else:
        print(a[i])
        c=c+1
print(c)
