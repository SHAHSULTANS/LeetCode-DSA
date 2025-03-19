from typing import Counter, List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary={}
        for index,item in enumerate(nums):
            dictionary[item]=index
            
        for index,item in enumerate(nums):
            value=target-item
            if dictionary[value] and index!=dictionary[value]:
                return [index,dictionary[value]]
                
        
        
        


# nums = [2,7,11,15]
# target = 9

# ob=Solution()
# print(ob.twoSum(nums,target))

# s="shanto ali"
# container=(Counter(s))
# print(max(container))
# print(container[' '])