

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        myset=set()
        ans=0
        l=0
        for i in range(n):
            while s[i] in myset:
                myset.remove(s[l])
                l+=1
            
            myset.add(s[i])
            ans=max(ans,i-l+1)
        return ans
            
            
    #     for i in range(0,n):
    #         # print(i)
    #         dic={}
    #         flag=False
    #         for j in range(i+1):
    #             if not dic.get(s[j]):
    #                 dic[s[j]]=1
    #             else:
    #                 dic[s[j]]+=1
    #         if self.reapeatOrnot(dic):
    #             ans=max(ans,i+1)
    #             flag=True
    #             continue
    #         ctn=0
    #         for j in range(i+1,n):
    #             if not dic.get(s[j]):
    #                 dic[s[j]]=1
    #             else:
    #                 dic[s[j]]+=1
    #             dic[s[ctn]]-=1
    #             ctn+=1
    #             if self.reapeatOrnot(dic):
    #                 ans=max(ans,i+1)
    #                 flag=True
    #                 break
    #         if not flag:
    #             break
    #     return ans
    
    # def reapeatOrnot(self,dic):
    #     for key in dic:
    #         if dic[key]>1:
    #             return False
            
    #     return True
        

s = "bbbbba"
ob=Solution()
print(ob.lengthOfLongestSubstring(s))