class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s={}
        for index,char in enumerate(s):
            if dic_s.get(char):
                ans=dic_s[char]
                ans.append(index)
                dic_s[char]=ans
            else:
                ans=[]
                ans.append(index)
                dic_s[char]=ans
        
        dic_t={}
        for index,char in enumerate(t):
            if dic_t.get(char):
                ans=dic_t[char]
                ans.append(index)
                dic_t[char]=ans
            else:
                ans=[]
                ans.append(index)
                dic_t[char]=ans
        
        covered={}
        ans_flag=True
        
        for index in range(len(s)):
            if not covered.get(s[index]):
                var1=dic_s[s[index]]
                var2=dic_t[t[index]]
                if var1!=var2:
                    ans_flag=False
                    break
                covered[s[index]]=1
        return ans_flag
                
            
s = "egg"
t = "add"
ob=Solution()
print(ob.isIsomorphic(s,t))

