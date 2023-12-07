# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
            self.rlt = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr = ''
        if not root:
             return []
        self.checkPath(root,arr)
        return self.res
    
    def checkPath(self,node,arr):
        newarr = arr + str(node.val)
        if not node.left and not node.right:
            self.rlt.append(newarr)
            return
        else:
            newarr = newarr + '->'
            if node.left:
                self.checkPath(node.left, newarr)
            if node.right:
                self.checkPath(node.right, newarr)  
        return