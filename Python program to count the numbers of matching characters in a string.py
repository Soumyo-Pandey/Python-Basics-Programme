import re 
a = input("Enter first string: ")
b = input("Enter second string: ")

c = 0
for i in a:
    if re.search(i,b):
        c = c + 1 
print("No. of matching characters are",c)