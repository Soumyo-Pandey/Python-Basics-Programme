a = int(input("Enter the start range: "))
z = int(input("Enter the end of the range:"))

for num in range(a,z + 1):
    
    if num % 2 != 0:
        print(num, end = " ")