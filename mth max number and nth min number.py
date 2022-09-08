a=[]
n=int(input("Enter the number of elements:"))
for i in range(1,10):
    b=int(input("Enter the elements:"))
    a.append(b)
x=max(a)+min(a)
y=max(a)-min(a)
print(x,y)
