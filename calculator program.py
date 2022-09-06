def add(x,y):
  return x+y
def sub(x,y):
  return x-y
def mul(x,y):
  return x*y
def div(x,y):
  return x/y
select=int(input("select the operation 1,2,3,4:"))
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
if select==1:
    print(num1,"+",num2,"=",(num1+num2))
elif select==2:
    print(num1,"-",num2,"=",(num1-num2))
elif select==3:
    print(num1,"*",num2,"=",(num1*num2))
elif select==4:
    print(num1,"/",num2,"=",(num1/num2))
else:
    print("invalid input")
