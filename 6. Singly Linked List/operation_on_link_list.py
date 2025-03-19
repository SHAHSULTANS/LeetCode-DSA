

from hmac import new
from tkinter import NO


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        

class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        current=self.head
        while current:
            yield current
            current=current.next    
        
    def insert_node(self,data,location=None):
        
        new_node=Node(data)
        
        if not self.head:
            
            self.head=new_node
            self.tail=new_node
        else:
            
            if location==0:
                
                new_node.next=self.head
                self.head=new_node
            elif location:
                
                current=self.head
                index=0
                
                while current and index<location-1:
                    index+=1
                    current=current.next
                    
                if not current:
                    raise IndexError("Location is out of bounds")    
                
                new_node.next=current.next
                current.next=new_node
            else:
                
                self.tail.next=new_node
                self.tail=new_node
                
                

    def delete_node(self,location=None):
        if self.head is None:
            print("The SLL doesn't exists!")
        else:
            if location==0:
                
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    
            elif location:
                current=self.head
                index=0
                
                while current and index<location-1:
                    index+=1
                    current=current.next
                
                if not current or not current.next:
                    raise IndexError("index out of range")
                
                current.next=current.next.next 
            else:
                
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    current=self.head
                    
                    while current:
                        if current.next==self.tail: 
                            break
                        current=current.next
                    
                    current.next=None
                    self.tail=current
                
            
            
                
                
    def display_all_nodes(self):
        if not self.head:  # If the list is empty
            print("There is no existing node")
            return

        current = self.head
        while current: 
            print(current.data, end=" -> ")
            current = current.next

        print("None")  # Indicate the end of the list
            
            
            
            
sll = SLinkedList()
sll.insert_node(10)           # Insert at the end (default)
sll.insert_node(20)           # Insert at the end (default)
sll.insert_node(5, 0)         # Insert at the beginning
sll.insert_node(15, 2)        # Insert in the middle (at position 2)

sll.display_all_nodes()
print("\nAlternative traverse: ")
nodevalue=[node.data for node in sll]
print(nodevalue)

print("\nDelete Operation\n")
sll.delete_node()
sll.display_all_nodes()

