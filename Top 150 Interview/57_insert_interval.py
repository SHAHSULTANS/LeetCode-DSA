from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        srt_inteval=sorted(intervals)
        n=len(srt_inteval)
        # if n==1:
        #     return 
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