


import numpy


twoDar=numpy.array([[1,4,5],[4,5,6], [7,8,9]])
oned=numpy.array([1,5,6])

# print(oned)
# print(type(oned))


print(twoDar)

# newarray=numpy.insert(twoDar,1,oned,axis=0)
newarray=numpy.append(twoDar,[oned],axis=0)
print(newarray[0])