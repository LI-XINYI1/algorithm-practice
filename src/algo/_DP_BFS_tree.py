
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution102:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
          return []
        levels = []
        que = []
        que.append(root)
        while len(que) > 0:
          level = []
          for i in range(len(que)):
            x = que.pop(0)
            level.append(x.val)
            if x.left is not None:
                que.append(x.left)
            if x.right:
                que.append(x.right)
          levels.append(level)
        return levels
    
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
          return []
        levels = []
        que = []
        que.append(root)
        zigzag = 0
        while len(que) > 0:
          level = []
          for i in range(len(que)):
            x = que.pop(0)
            level.append(x.val)
            if x.left is not None:
                que.append(x.left)
            if x.right:
                que.append(x.right)
          if zigzag % 2 == 1:
             level.reverse()
          zigzag += 1
          levels.append(level)
        return levels     

class Solution107:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
          return []
        levels = []
        que = []
        que.append(root)
        while len(que) > 0:
          level = []
          for i in range(len(que)):
            x = que.pop(0)
            level.append(x.val)
            if x.left is not None:
                que.append(x.left)
            if x.right:
                que.append(x.right)
          levels.append(level)
        
        return levels[::-1]   

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution429:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
      if not root:
         return []
      levels = []
      que = []
      que.append(root)
      while len(que) > 0:
          level = []
          for i in range(len(que)):
            x = que.pop(0)
            level.append(x.val)
            # children here is a list of Nodes,
            # so += instead of append!!!!!!!!!
            que += x.children  
          levels.append(level)
      return levels
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1161:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
          return []
        levels = []
        maxval = -float('inf')
        flag = 0
        rlt = 0
        que = []
        que.append(root)
        while len(que) > 0:
          level = []
          sumval = 0
          for i in range(len(que)):
            x = que.pop(0)
            level.append(x.val)
            sumval += x.val
            if x.left is not None:
                que.append(x.left)
            if x.right:
                que.append(x.right)
          levels.append(level)
          if sumval > maxval:
            maxval = sumval 
            rlt = len(levels)
        return rlt  
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution199:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        result = []
        queue=deque([root])

        while queue:
            level_length=len(queue)
            for i in range(level_length):
                node=queue.popleft()
                if i==level_length-1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution515:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        l=defaultdict(list)
        def traversal(root,h):
            if root is None:
                return
            l[h].append(root.val)
            traversal(root.left,h+1)
            traversal(root.right,h+1)
        traversal(root,0)
        res=[]
        for i in l.values():
            res.append(max(i))
        return res
    
