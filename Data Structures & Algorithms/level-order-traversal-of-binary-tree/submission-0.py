# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [[root, 0]]
        res = []

        while q:
            top, depth = q.pop()
            if top is None: continue

            if depth + 1 > len(res):
                res.append([])
            
            res[depth].append(top.val)

            q.append([top.right, depth + 1])
            q.append([top.left, depth + 1])
        
        return res