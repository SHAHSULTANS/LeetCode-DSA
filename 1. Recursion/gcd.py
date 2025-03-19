
def gcd(a,b):
    if(b==0):
        return a
    if(a%b==0):
        # print(a%b)
        # print(b)
        return b
        
    return gcd(b,a%b)
    
print(gcd(0,12))