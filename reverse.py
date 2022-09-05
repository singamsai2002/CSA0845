#author sai 2002 05/09/2022
def reverse_string(s):
    str=" "
    for i in s:
        str = i + str
    return str
s = "water"
print("original string is:",end=" ")
print(s)
print("reverse string is:",end=" ")
print(reverse_string(s))
    
    
    
