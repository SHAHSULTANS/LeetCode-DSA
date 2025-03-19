


from queue import Queue
import queue


class TreeNode:
    
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
        


root=TreeNode("Drinks")

cold=TreeNode("cold")
hot=TreeNode("hot")
root.leftchild=cold
root.rightchild=hot


cold1=TreeNode("cold1")
cold.leftchild=cold1





def preorder(root):
    if root is None:
        return

    print(root.data)
    preorder(root.leftchild)
    preorder(root.rightchild)
    
    
preorder(root)
    

