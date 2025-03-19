from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n=len(nums)
        ans=[]
        if n==1:
            return [f"{nums[0]}"]
        i=0
        while i<n-1:
            l=r=i
            while i<n-1 and nums[i]+1==nums[i+1]:
                i+=1
                r+=1
            print(i)    
            if i==n-1:
                ans.append(f"{nums[l]}->{nums[r]}")
                break  
            elif i==n-2 and nums[i]+1!=nums[i+1]:
                if l!=r:
                    ans.append(f"{nums[l]}->{nums[r]}")
                    ans.append(f"{nums[i+1]}")
                    
                else:
                    ans.append(f"{nums[i]}")
                    ans.append(f"{nums[i+1]}")
                    break
            else:
                if l!=r:
                    ans.append(f"{nums[l]}->{nums[r]}")
                else:
                    ans.append(f"{nums[l]}")
                    
            i+=1
        return ans
                    

            