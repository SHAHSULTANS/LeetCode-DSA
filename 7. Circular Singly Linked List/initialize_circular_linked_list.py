


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class circularSLL:
    def __init__(self):
        self.head=None
        self.tail=None
     
    def __iter__(self):
        node=self.head
        while node:
            yield node
            if node.next==self.head:
                break
            node=node.next 
            
    def createCirSLL(self,nodevalue):
        node=Node(nodevalue)
        node.next=node
        self.head=node
        self.tail=node
        return "The CSLL has been created."
    
    
CSLLob=circularSLL()
CSLLob.createCirSLL(5)
print([node.value for node in CSLLob])
 
        