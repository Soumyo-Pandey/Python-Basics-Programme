a = (input("Enter a string as your choice:"))

print("The original string is : " + str(a))

hlf_idx = len(a) // 2

res = ' '
for idx in range(len(a)):
    
    if idx >= hlf_idx:
        res += a[idx].upper()
    else:
        res += a[idx]
print("The resultant string:" + str(res))