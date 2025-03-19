

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         hashmpap={}
        
#         while True:
#             sqsum=self.fun(n)
#             n=sqsum
#             # print(sqsum)
#             # break
#             if sqsum==1:
#                 return True
            
#             try:
#                 hashmpap[sqsum]+=1
#                 return False
#             except:
#                 hashmpap[sqsum]=1
       
#     def fun(self,n):
#         num=n
#         sum=0
#         while num!=0:
#             lasdigit=num%10
#             sum+=(lasdigit*lasdigit)
#             num=num//10 
#         return sum   
    
    
# ob=Solution()
# n=19

# print(ob.isHappy(n)) 
            

            
            
            
            
class Solution:
    def isHappy(self, n: int) -> bool:
        if(n==1 or n==7):
            return True
        else:
            sum =0
            while(n>0):
                temp = n%10
                sum += temp*temp
                n= n//10
            return self.isHappy(sum) 
        