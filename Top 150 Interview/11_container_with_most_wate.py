from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i,j=0,len(height)-1
        ans=0
        
        while(i<j):
            x_axies=j-i
            y_axies=min(height[i],height[j])
            ans=max(ans,(x_axies*y_axies))
            
            if height[i]<height[j]:
                i+=1
            elif height[i]>height[j]:
                j-=1
            else:
                i+=1
        
        return ans
    
    

height = [1,8,6,2,5,4,8,3,7]
ob=Solution()
  
print(ob.maxArea(height))