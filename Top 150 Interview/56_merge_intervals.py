
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        srt_inteval=sorted(intervals)
        n=len(srt_inteval)
        ans=[]
        ans.append(srt_inteval[0])
        
        for i in range(1,n):
            prev=ans.pop()
            current=srt_inteval[i]
            # print(current)
            if prev[1]>=current[0]:
                # print(prev[1]," ",current[1])
                if prev[1]<current[1]:
                    prev[1]=current[1]
                    # print(ans)
                ans.append(prev)
            else:
                ans.append(prev)
                ans.append(current)
                
        return ans
            
intervals = [[1,3],[2,6],[8,10],[15,18]]

ob=Solution()
print(ob.merge(intervals))
