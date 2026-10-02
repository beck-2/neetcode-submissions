# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #use dp? or dfs... in order processing?
        #recursive wayyy better than iterative dfs tbh
        res=0
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            #split
            nonlocal res
            leftmax=dfs(root.left)
            rightmax=dfs(root.right)
            res = max(res, leftmax + rightmax)
            #no split
            return 1+max(leftmax, rightmax)
        dfs(root)
        return res
        
        