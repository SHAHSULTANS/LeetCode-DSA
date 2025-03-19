from typing import Counter,List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for item in strs:
            ans=sorted(item)
            ans=str(ans)
            if dic.get(ans):
                dummy=dic[ans]
                dummy.append(item)
                dic[ans]=dummy
            else:
                dummy=[]
                dummy.append(item)
                dic[ans]=dummy
        return [dic[key] for key in dic]









# from typing import Counter


# nums=[1,4,5,6,7]
# ans=Counter(nums)
# print(ans)
# ans.pop(1)
# print()
# print(ans[8])
# print()
# print(ans)