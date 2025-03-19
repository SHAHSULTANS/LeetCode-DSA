

mydic={"name":"shanto","age":24,"working":True,"something":False}


print("name" in mydic)
print("shanto" in mydic.values())

############################################3
#In python any(iterable), all(iterable) method takes iterable arguments.

#all() method
newdic={0:True, 2:False}
print("\nall() method")
print(all(newdic))


#any() method
print("\nany() method")
print(any(newdic))



#sorted(iteratble, reverse,key) method