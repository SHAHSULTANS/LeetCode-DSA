from collections import deque


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans=k
        n=k
        summation=0
        afterone=0
        q=deque()
        for item in nums:
            if item==1:
                afterone+=1
                summation+=1
            else:
                print(q)
                if n>=1:
                    n=n-1
                    q.append(afterone)
                else:
                    q.append(afterone)
                    ans=max(ans,summation+k)
                    # print(ans)
                    # if q:
                    top=q.popleft()
                    summation-=top
                    # print("summation", summation, " top",top)
                afterone=0
         
        ans=max(ans,summation+(k-n))
        
        return ans