
def flatten(ar):
    result=[]
    for item in ar:
        if isinstance(item,list):
            result+=flatten(item)
        else:
            result.append(item)
    return result




var=[[[[1]]],[[2]],[[[[[[[[[[[5]]]]]]]]]]]]

print(flatten(var))