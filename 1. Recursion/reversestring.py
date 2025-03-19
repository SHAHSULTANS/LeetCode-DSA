

# def reverseString(stng):
#     if(len(stng)==0):
#         return ""
    
#     print(stng[len(stng)-1],end="")
#     return reverseString(stng[:-1])


# var="shanto"
# reverseString(var)
# # print(var[:-1])



  


def reverse(s):
    n=len(s)
    if n<=1:
        return s
    
    left,right=s[0],s[n-1]
    newst=s[1:n-1]
    return right+reverse(newst)+left


s="shanto"
print(reverse(s))
print(s)