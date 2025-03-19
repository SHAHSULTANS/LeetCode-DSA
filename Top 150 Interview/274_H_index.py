from typing import List
from xmlrpc.client import Boolean

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans=0
        l,r=0,1010
        while l<=r:
            mid=int((l+r)/2)
            
            if self.midpoint_check(citations,mid):
               ans=mid
               l=mid+1
            else:
                r=mid-1
    
        return ans
     
     
        # #solution 2:
        # n=len(citations)
        # citations.sort()
        
        # for index,value in enumerate(citations):
        #     if v>=n-i:
        #         return n-i
        
        # return 0
            
            
    def midpoint_check(self,citations,mid)->Boolean:
        # print(citations)
        ctn=0
        for items in citations:
            if items>=mid:
                ctn+=1
        return ctn>=mid
    
   
    
    
    
citations = [3,0,6,1,5]
ob=Solution()
ob.hIndex(citations)