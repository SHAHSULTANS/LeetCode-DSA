
def sum_of_digit(n):
    assert n>=0 and int(n)==n, "The number has to be a positive integer."
    if(n==0):
        return n
    
    return (n%10)+sum_of_digit(int(n/10))

print(sum_of_digit(-1231))