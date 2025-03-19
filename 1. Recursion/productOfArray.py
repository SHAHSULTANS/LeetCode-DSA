

def productOfArray(arr):
    if(len(arr)==0):
        return 1
    return arr[0]* productOfArray(arr[1:])

print(productOfArray([1,3,10]))#30
print(productOfArray([1,2,3,10])) #60