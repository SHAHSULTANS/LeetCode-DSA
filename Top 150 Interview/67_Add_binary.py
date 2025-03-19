from pyparsing import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=a[::-1]
        b=b[::-1]
        n1=len(a)
        n2=len(b)
        ans=deque()
        print(a)
        print(b)
        
        i,j,rem=0,0,0
        
        while i<n1 or j<n2:
            bit1=a[i] if i<n1 else 0
            bit2=b[j] if j<n2 else 0
            bit1=int(bit1)
            bit2=int(bit2)
            # print(bit1," ",bit2)
            
            if bit1==bit2 and bit1==1:
                if rem==1:
                    ans.appendleft('1')
                else:
                    ans.appendleft('0')
                rem=1
            elif bit1==bit2 and bit1==0:
                if rem:
                    ans.appendleft('1')
                    rem=0
                else:
                    ans.appendleft('0')
            elif bit1 or bit2:
                if rem:
                    ans.appendleft('0')
                    rem=1
                else:
                    ans.appendleft('1')
                    rem=0
            i+=1
            j+=1
            # print(''.join(ans))
        # print(ans)
        if rem:
            ans.appendleft('1')
        return ''.join(ans)

        
                    
            