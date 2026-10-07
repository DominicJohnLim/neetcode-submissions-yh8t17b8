# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        current_path = []
        p_path, q_path = [], []
        def helper(node):
            nonlocal p_path, q_path
            if node is None: return

            current_path.append(node)

            if node is p:
                p_path = current_path.copy()

            if node is q:
                q_path = current_path.copy()

            helper(node.left)
            helper(node.right)

            current_path.pop()
        
        helper(root)

        last_common = root
        
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] == q_path[i]:
                last_common = p_path[i]

        return last_common