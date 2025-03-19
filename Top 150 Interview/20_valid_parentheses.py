class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        
        for char in s:
            if char in [')',']','}']:
                n=len(stk)
                if not n:
                    return False
                else:
                    if char==')' and stk[n-1]=='(' or char==']' and stk[n-1]=='[' or char=='}' and stk[n-1]=='{':
                        stk.pop()
                    else:
                        return False
            else:
                stk.append(char)
                
        return len(stk)<=0