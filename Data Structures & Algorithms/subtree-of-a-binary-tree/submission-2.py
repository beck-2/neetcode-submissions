# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)
        #quite similar to last one... use it as a helper function
    def isSametree(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if r is None and s is None:
            return True
        if r and s and r.val==s.val and self.isSametree(r.left,s.left) and self.isSametree(r.right,s.right):
            return True
        else:
            return False
        