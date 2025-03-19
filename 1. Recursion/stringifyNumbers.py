


def stringifNumbers(obj):
    for key in obj:
        if type(obj[key]) is int:
            obj[key]=str(obj[key])
        if isinstance(obj[key],dict):
            stringifNumbers(obj[key])
    
    return obj







obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}
print(obj)
stringifNumbers(obj)
print(obj)