
def recur(nums):
    res=[]
    for item in nums:
        if isinstance(item,list):
            res+=recur(item)
        else:
            res.append(item)
            
    return res


nums=[[[1]],[[[[2]]]]]

print(recur(nums))

