
from typing import List

from numpy import divide

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        
        for item in tokens:
            if item in ['+', '-', '*','/']:
                a=int(stk.pop())
                b=int(stk.pop())
                res=0
                if item=='/':
                    res=int(a/b)
                elif item=="+":
                    res=a+b
                elif item=="-":
                    res=a-b
                elif item=="*":
                    res=a*b
                stk.append(res)
                
            else:
                stk.append(item)
        
        return stk[0]
        
# nums=["1,",'4']
# nums[1]=int(nums[1])
# print(type(nums[1]))

print ((1//(-132)))
