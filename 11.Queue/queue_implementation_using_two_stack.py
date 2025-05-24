class Solution:
    def __init__(self):
        self.push_stack=[]
        self.pop_stack=[]
        
    def enqueue(self,value):
        #Move all element pop stack to push stack
        while self.pop_stack:
            self.push_stack.append(self.pop_stack.pop())
        
        #append new to push stack
        self.push_stack.append(value)
        
        #Then again all value push stack to pop stack
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
            
    
    def dequeue(self):
        if not self.pop_stack:
            return -1
        else:
            #Get top value of pop stack
            return self.pop_stack.pop()
    