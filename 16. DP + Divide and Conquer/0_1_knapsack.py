
#We have to use 2D array for memoization. If use python dictionary that is slower process. As a result it gives us TLE.

class Solution:
    def knapsack(self, W, val, wt):
        memo=[[-1]*(W+1) for _ in range(len(wt)+1)]
        
        def maximize_profit(W,val, wt,i,memo):
            if i==len(wt) or W==0:
                return 0
            if memo[i][W]!=-1:
                return memo[i][W]
                
            if wt[i]>W:
                memo[i][W]= maximize_profit(W,val,wt,i+1,memo)
                return memo[i][W]
            
            memo[i][W]= max(val[i]+maximize_profit(W-wt[i],val,wt,i+1,memo),maximize_profit(W,val,wt,i+1,memo))
            return memo[i][W]
        
        return maximize_profit(W,val,wt,0,memo)
    

#______________Real World Application of knapsack______________-#
        #🔒 Cargo Loading / Shipping
        #🎓 College Course Scheduling
        #🧳 Resource Allocation in Project Management

        
    
    
    
# class Solution:
#     def knapsack(self, W, val, wt):
        
#         def maximize_profit(W,val, wt,i,memo):
#             if i==len(wt):
#                 return 0

#             if wt[i]>W:
#                 memo[(i,W)]= maximize_profit(W,val,wt,i+1)
#                 return memo[(i,W)]
            
#             memo[(i,W)]= max(val[i]+maximize_profit(W-wt[i],val,wt,i+1),maximize_profit(W,val,wt,i+1))
#             return memo[(i,W)]
        
#         return maximize_profit(W,val,wt,0,{})
    
    
    
    
# dictionary={}
# dictionary[(2,4)]=5
# print(dictionary)






