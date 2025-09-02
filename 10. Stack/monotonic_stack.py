
nums=[4,1,5,6,2,0]

custom_stack=[]

for item in nums:
    while custom_stack and custom_stack[-1]<item:
        top=custom_stack.pop()  
        
        print(top,"----next greater-",item," ")
        # custom_stack.pop()
    else:
        custom_stack.append(item)
        
while custom_stack:
        
    top=custom_stack.pop()  
    print(top,"----next greater-","-1")

