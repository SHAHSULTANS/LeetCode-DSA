
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or len(s)<=numRows:
            return s
        
        iterate=numRows+(numRows-2)
        ans=[]
        
        
        for i in range(0,len(s),iterate):
            ans.append(s[i])
            
        if numRows-2>0:
            
            step=numRows-2
            for i in range(1,numRows-2+1):
                row=numRows
                for j in range(i,len(s),iterate):
                    ans.append(s[j])
                    if row+step-1<len(s):
                        # print(numRo)
                        # print(row,f" step {row+step-1} ",s[row],s[j])
                        ans.append(s[row+step-1])
                    
                    row+=iterate

                step-=1
                   
        
        for i in range(numRows-1,len(s),iterate):
            ans.append(s[i])
            
        return "".join(ans)
                    
            
             
            
        
        # print(i)
                
                    