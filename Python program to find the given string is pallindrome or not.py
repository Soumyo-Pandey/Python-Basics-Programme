def pallindrome(z):
    
    mid = (len(z)-1)//2
    start = 0
    last = len(z) - 1 
    flag = 0
    
    while(start < mid):
        
        if(z[start]== z[last]):
            
            start += 1 
            last -= 1 
        else:
            flag = 1 
            break;
    if flag == 0:
        print("The entered string is pallindrome")
    else:
        print("The entered string is not pallindrome")
def symmetry(z):
    
    n = len(z)
    flag = 0
    
    if n % 2:
        mid = n//2 + 1 
    else:
        mid = n//2
    
    start1 = 0
    start2 = mid
    
    while(start1 < mid and start2 < n):
        
        if(z[start1] == z[start2]):
            start1 = start1 + 1 
            start2 = start2 + 1 
        else:
            flag = 1 
            break
        
        if flag == 0:
            print("The entered string is symmetrical")
        else:
            print("The entered string is not symmetrical")
            
string = 'soumyo amamama'
pallindrome(string)
symmetry(string)