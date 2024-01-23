import sys

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

    def levelOrder(self,root):
        if root is not None:
            queue = [root]
            output = ''
            while len(queue) > 0:
                if (queue[0].left is not None):
                    queue.append(queue[0].left)
                if (queue[0].right is not None):
                    queue.append(queue[0].right)
                output += str(queue.pop(0).data) + ' '
            print(output)
                

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
