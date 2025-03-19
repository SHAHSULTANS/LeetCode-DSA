
# class Author:
#     def __init__(self,name,age,org):
#         self.name=name
#         self.age=age
#         self.org=org


        

# class Book(Author):
#     def __init__(self, name, age, org,bookname,price):
#         super().__init__(name, age, org)
#         self.bookname=bookname
#         self.price=price
        
    
#     def discout(self,dis_percentage):
#         """This function calculate discount. set the price after discount"""
#         dis_count=(self.price*dis_percentage)/100
#         self.price=self.price-dis_count
        
   
    
# book1=Book("shanto",24,"joykoli","chemistry_bithitra",500)


# print(book1.age)
# book1.discout(25)
# print(book1.price)

# # print(hash("shanto"))


# table={
#     "id":1,
#     "name":"shanto",
#     "email":"---@gmail.com"
# }
        
        
import copy


ar=[2,4,6]
num=ar
num[0]=10
print(id(num)==id(ar))

print(ar)
        