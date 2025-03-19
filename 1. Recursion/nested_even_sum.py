
def even_sum(obj):
    sum=0
    for key in obj:
        if isinstance(obj[key],int) and obj[key]%2==0:
            sum+=obj[key]
        if isinstance(obj[key],dict):
            sum+= even_sum(obj[key])
            
    return sum






obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

print(even_sum(obj2))#10