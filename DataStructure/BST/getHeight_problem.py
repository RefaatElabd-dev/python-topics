class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    
    def getHeight(self, root):
        return self.getLevels(root) - 1
    
    def getLevels(self, root):
        if(root is None): 
            return 0
        return max(self.getLevels(root.left),self.getLevels(root.right))+1
        
        
from math import log2, ceil
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)