




from requests import head


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
    
    def insertCSLL(self,value,location=None):
        if self.head is None:
            return "The head ref is None"
        else:
            newnode=Node(value)
            try:
                # print(location)
                if location==0:
                    newnode.next=self.head
                    self.head=newnode
                    self.tail.next=newnode
                elif location is None:
                    # print(location)
                    newnode.next=self.head
                    self.tail.next=newnode
                    self.tail=newnode
                else:
                    current=self.head
                    index=0
                    while index<location-1:
                        current=current.next
                        index+=1
                    newnode.next=current.next
                    current.next=newnode
                   
                return "Successfully Inserted"
            except:
                return "Insert Out of range"
            
            
    def deleteNode(self, location=None):
        if self.head is None:
            print("There is not any node in CSLL")
            return
        
        if location==0:
            
            if self.head==self.tail:
                self.head.next=None
                self.tail.next=None
            else:
                self.head=self.head.next
                self.tail.next=self.head
        elif location is None:
            
            if self.head==self.tail:
                self.head.next=None
                self.tail.next=None
            else:
                current=self.head
                while current:
                    if current.next==self.tail:
                        break
                    current=current.next
                
                current.next=self.head
                self.tail=current
        else:
            current=self.head
            index=1
            
            while index<location-1:
                current=current.next
                index+=1
            
            current.next=current.next.next 
                
    
    
CSLLob=circularSLL()
CSLLob.createCirSLL(5)
CSLLob.insertCSLL(0,0)
CSLLob.insertCSLL(1,1)
CSLLob.insertCSLL(4,2)
print(CSLLob.insertCSLL(10))

print([node.value for node in CSLLob])
        

# CSLLob.deleteNode(0)
# print([node.value for node in CSLLob])

# CSLLob.deleteNode()
# print([node.value for node in CSLLob])



CSLLob.deleteNode(1)
print([node.value for node in CSLLob])
    
