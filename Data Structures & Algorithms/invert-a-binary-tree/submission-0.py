from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop()
            if node == None:
                break
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            # swap left and right
            temp = node.left
            node.left = node.right
            node.right = temp

        return root