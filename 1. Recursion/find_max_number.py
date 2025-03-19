
numbers=[4,10,45,9,30,20]

def maxnumber(ar,n):
    if(n==1):
        return ar[0]
    
    return max(ar[n-1],maxnumber(ar,n-1))

print(maxnumber(numbers,len(numbers)))