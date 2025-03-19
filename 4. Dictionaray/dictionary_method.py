

mydic={"name":"Shanto","age":24,"working":True}
anothercopy=mydic.copy()

anothercopy["Town"]="sherpur"

print(mydic)
print(anothercopy)


#get method
print()
print(mydic.get("shan"))
# print(mydic["shan"])


#update() method
print("\nUpdate method")
mydic.update({"a":1,"b":1,"c":2})
print(mydic)



#item() method
print()
print(mydic.items())
# for key,value in mydic.items():
#     print(key," ",value)


#keys() method
print()
print(mydic.keys())

#popitem() method remvoe a arbitary elements.

print("\npopitem() method")
print(mydic.popitem())


#setdefault() method
#if key exits then return value, else insert key and default value.
print()
print(mydic.setdefault("first_name","shah"))
print(mydic)