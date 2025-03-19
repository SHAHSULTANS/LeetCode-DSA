
from typing import Counter


class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split("/")
        ans=[]
        
        for p in path:
            if p=='.' or p=='':
                continue
            if p=='..':
                if len(ans):
                    ans.pop()
            else:
                ans.append(p)    
        
        return "/"+"/".join(ans)
            
        # ans=['/']
        # for i in range(1,len(path)):

        #     if len(ans)>0 and ans[-1]!='/' or len(ans)==0:
        #         ans.append("/")

        #     n=len(path[i])
        #     if n==0:
        #         if len(ans)>0:
        #             if ans[-1]!='/':
        #                 ans.append("/")
        #         else:
        #             ans.append("/")
        #         # print(ans,"   ->",i)
        #     elif n==2:
        #         hmap=Counter(path[i])
        #         if hmap['.']==2:
        #             for j in range(min(len(ans),2)):
        #                 print(ans)
        #                 ans.pop()
        #         else:
        #             ans.append(path[i])
        #     else:
        #         if n==1 and path[i]=='.':
        #             pass
        #         else:
        #             ans.append(path[i])
                    
        # if len(ans)>0 and ans[-1]=='/':
        #     ans.pop()
        # if len(ans)==0:
        #     ans.append("/")
        
        # # print(ans)
        # return "".join(ans)
                
        
    
    
ob=Solution()
path = "/home/user/Documents/../Pictures/"
print(path.split("/"))
print(ob.simplifyPath(path))


                
            
                