

numbers=[1,2]
mydic={"name":"shanto","age":24}
print(mydic)


#Touple value always hash. 
print()
mytouple=(1,2)
print(hash(mytouple))


#Rarely hash value may collision. But python have special algorithm (like addressing change) to avoid collision.
print()
# Two different keys with the same hash value (collision simulated)
key1 = "name"
key2 = "eman"  # Anagrams can sometimes lead to hash collisions

print(hash(key1))  # Outputs the hash value
print(hash(key2))  # May output the same hash value