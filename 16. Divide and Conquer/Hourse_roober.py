

def robber_profit(i,memo):
    if i<0:
        return 0
    if i in memo:
        return memo[i]
    
    memo[i]= max(robber_profit(i-1,memo),profit[i]+robber_profit(i-2,memo))
    return memo[i]

profit=[5,4,20,50,20,5,70]

print(robber_profit(len(profit)-1,{})) 

