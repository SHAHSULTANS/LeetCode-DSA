def dcimal_to_binary(n):
    # print(n)
    if(n<=1):
        print(n, end="")
        return
    
    dcimal_to_binary(int(n/2))
    print(n%2, end="")
    
dcimal_to_binary(8)