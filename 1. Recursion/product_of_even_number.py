
  
def product_of_even_number(index,l1):
    if index==len(l1):
        return 1
    
    val=1
    if l1[index]%2==0:
        val=l1[index]
    
    return product_of_even_number(index+1,l1)*val


nums=[1,7,5,3]

print(product_of_even_number(0,nums))