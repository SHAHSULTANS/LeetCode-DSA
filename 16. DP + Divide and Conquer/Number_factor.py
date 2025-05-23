#Write a function that returns the number of ways to express a given number n as a sum of 1, 3, and 4.


def number_of_ways(n):
    if n in [0,1,2]:
        return 1
    elif n==3:
        return 2
    
    return number_of_ways(n-1)+number_of_ways(n-3)+number_of_ways(n-4)

print(number_of_ways(4))