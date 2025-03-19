from typing import Counter, List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        # newarry=[nums[index] for index in range(0,min(k+1,n))]
        # print(newarry)
        hashmap=Counter(nums[:min(k+1,n)])
        # print(hashmap)
        
        ctn=0
        ans=False
        for key in hashmap:
            if hashmap[key]>1:
                ans=True
        
        if ans:
            return ans
        
        for index in range(k+1,n):
            # print(item)
            hashmap[nums[index]]+=1
            hashmap[nums[ctn]]-=1
            
         
            if hashmap[nums[index]]>1:
                ans=True
                
            ctn+=1
        
        return ans
    
    
    
print(25**0.5)

print(50%10)