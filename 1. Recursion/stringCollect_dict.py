

def stringCollect(obj):
    result=[]
    for key in obj:
        if isinstance(obj[key],str):
            result.append(obj[key])
        if isinstance(obj[key],dict):
           result+= stringCollect(obj[key])
        
    return result








obj = {
  "stuff": 'shanto',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

print(stringCollect(obj))