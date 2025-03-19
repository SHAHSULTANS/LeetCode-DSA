

from array import*


myarray=array("i",[1,2,3,5,6])
print(myarray)
myarray.append(19)
myarray.reverse()
myarray.pop(0)
myarray.insert(0,20)
for item in myarray:
    print(item)