






from collections import deque


class Solution:
    def __init__(self):
        self.dog_enque=deque()
        self.cat_enque=deque()
        self.time=0
    
    def enqueue(self,text):
        self.time+=1
        if text=="dog":
            self.dog_enque.appendleft((text,self.time))
        else:
            self.cat_enque.appendleft((text,self.time))
            
    def deque_any(self):
        if not self.cat_enque and not self.dog_enque:
            print("NO Animals")
            return
        
        if not self.cat_enque:
            self.dog_enque.pop()
            print("dog")
        elif not self.dog_enque:
            self.cat_enque.pop()
            print("cat")
        
        elif self.dog_enque[-1][1]<self.cat_enque[-1][1]:
            self.dog_enque.pop()
            print("dog")
        else:
            self.cat_enque.pop()
            print("cat")
            
    def deque_dog(self):
        if self.dog_enque:
            self.dog_enque.pop()
            print("dog")
        else:
            print("No dogs")
    
    def deque_cat(self):
        if self.cat_enque:
            
            self.cat_enque.pop()
            print("cat")
        else:
            print("No cats")
        
        
        

    
# num=[]
# num.append(5)
# num.append(6)
# print(num.pop())  

# q=deque()
# q.appendleft(6)
# q.appendleft(7)

# print(q.pop())





