#author sai 2002 05/09/2022
def reverse_number(s):
    number=" "
    for i in s:
        number = i + number
    return number
s = "1234"
print("original number is:",end=" ")
print(s)
print("reverse number is:",end=" ")
print(reverse_number(s))
    
    
    
