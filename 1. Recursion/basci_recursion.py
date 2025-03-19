
def BasciRecursion(n):
    if(n<1):
        print("n is less than 1")
    else:
        BasciRecursion(n-1)
        print(n)
        
BasciRecursion(4)