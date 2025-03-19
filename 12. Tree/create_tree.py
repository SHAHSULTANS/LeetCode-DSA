


class TreeNode:
    
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children
        
    def __str__(self,level=0):
        ret="  "*level+self.data+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)
            
        return ret
    
    def addChild(self,child):
        self.children.append(child)
        
        
root=TreeNode("Drinks",[])

cold=TreeNode("cold",[])
hot=TreeNode("hot",[])

hot1=TreeNode("cappucino",[])
hot2=TreeNode("americano",[])

hot.addChild(hot1)
hot.addChild(hot2)

root.addChild(hot)
root.addChild(cold)



print(root)