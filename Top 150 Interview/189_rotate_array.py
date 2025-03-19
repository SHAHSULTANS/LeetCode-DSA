from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)
        k=k%n
        rotoate=[0]*n
        print(rotoate)
        for i in range(n):
            rotoate[(i+k)%n]=nums[i]
            
        for i in range(n):
            nums[i]=rotoate[i]
        # copy=[]
        # k=k%len(nums)
        # index=-1
        # for i in range(k):
        #     index=len(nums)-i-1
        #     copy.append(nums[index])
        #     nums[index]=nums[index-k]
        
        # while  index-k>=0:
        #     nums[index]=nums[index-k]
        #     index-=1
        
        # for a in range(k):
        #     nums[a]=copy[k-a-1]
        # # print(index)
        # print(nums)
        # print(copy)
        
        
nums=[1,111,1,1,1]
k =2

ob=Solution()

ob.rotate(nums,k)