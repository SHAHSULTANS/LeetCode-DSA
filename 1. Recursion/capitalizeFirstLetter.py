

def capitalizeFirstLetter(ar):
    result=[]
    if(len(ar)==0):
        return [] #return list(for concate two list)
    
    # result.append(ar[0][0].upper()+ar[0][1:])
    result.append(ar[0].capitalize())
    return result+ (capitalizeFirstLetter(ar[1:]))





namelist=["shanto","sultan","md","aaa","bbb"]
# print(type(namelist[0]))
print(capitalizeFirstLetter(namelist))



# namelist2=["hasan","mahmud"]
# print(namelist[0].capitalize())
# print(namelist+namelist2)#concate 
# print(namelist[0][1:])#hanto