


class TreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        

class BinarySearchTree:
    def __init__(self):
        self.root=None
        
    def insert(self,key):
        if self.root is None:
            self.root=TreeNode(key)
        else:
            self.insert_recursively(self.root,key)
        
    def insert_recursively(self,node,key):
        if key<node.key:
            if node.left is None:
                node.left=TreeNode(key)
            else:
                self.insert_recursively(node.left,key)
        elif key>node.key:
            if node.right is None:
                node.right=TreeNode(key)
            else:
                self.insert_recursively(node.right,key)
        
    
    
    def search(self,key):
        return self.search_recursively(self.root,key)
    
    def search_recursively(self,node,key):
        if node is None or node.key==key:
            return node
        
        if key<node.key:
            self.search_recursively(node.left,key)
        else:
            self.search_recursively(node.right,key)
    
    
    def inorder(self):
        result=[]
        self.inorder_recursive(self.root,result)
        return result
    
    def inorder_recursive(self,node,result):
        if node:
            self.inorder_recursive(node.left,result)
            result.append(node.key)
            self.inorder_recursive(node.right,result)
            
    def delete(self,key):
        pass
            
                
bst=BinarySearchTree()    

bst.insert(50)
bst.insert(40)
bst.insert(45)
bst.insert(55)    

print(bst.inorder())