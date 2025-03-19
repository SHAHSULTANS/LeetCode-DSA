
from array import *

#create an array and traverse
myarray=array("i",[1,2,3,4,5]) 

for item in myarray:
    print(item ,end=" ")
print()



#append any value to the array using append() method
print("Append method")
myarray.append(6)
print(myarray)

#insert value in the array uing insert() method
print("\nInsert mehtod")
myarray.insert(0,11)
print(myarray)


#extend python array using extend() function
print("\nExtend my own array")
myarray.extend([20,30,40,50,30])
print(myarray)


#Add item from list into array using formlist() method.
print("\nfromlist function")
templist=[15,16,17]
myarray.fromlist(templist)
print(myarray)

#remove any array elment using remove() method
print("\nremove() method")
myarray.remove(20)
print(myarray)

#Fetch any element its index using index() method
print("\nIndex method()" )
print(myarray.index(50))

#reverse array using reverse() method()
print("\nreverse array")
myarray.reverse()
print(myarray)

#Get the buffer information through using buffer_infor() method
print("\nbuffer info array")
info=myarray.buffer_info()
print(info)


#check number of occurance any given number using count()
print("\nCount occurance")
ctn=myarray.count(30)
print(ctn)

#convert array to string using toString()
# print("\nConvert array to string")
# convetStr=myarray.tostring()
# print(convetStr)


#convet array to list using tolist()
print("\nConvert arrary to list")
print(myarray.tolist())


#slice the array element
print("\nSlice the array")
print(myarray[:])
