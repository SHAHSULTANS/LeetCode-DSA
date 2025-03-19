
# strng="a"
# print(strng[1:-1])
def ispalindrome(strng):
    if(len(strng)==0):
        return True
    if(strng[0]!=strng[len(strng)-1]):
        return False
    
    return ispalindrome(strng[1:-1])

print(ispalindrome("madam"))
print(ispalindrome("abcdcba"))

