from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        queue = deque()
        queue.append((root, 1))
        output = 0
        while len(queue) > 0:
            node, val = queue.pop()
            output = max(output, val)
            if node.left:
                queue.append((node.left, val + 1))
            if node.right:
                queue.append((node.right, val + 1))
        
        return output