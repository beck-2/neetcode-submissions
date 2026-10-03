# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #we should keep track of min seen and max seen for each path
        #i could literally build a bst and see if it matches
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float("-inf"), float("inf"))


        """ 
        if root is None:
            return True
        #postorder
        if not (self.isValidBST(root.left) and self.isValidBST(root.right)):
            return False
        if (root.left and root.left.val >= root.val) or (root.right and root.right.val <= root.val):
            return False
        return True
        
        #for third condition, recursively call this function on left and right subtrees
        #1:43
        if root is None:
            return True
        if (root.left and root.left.val>=root.val) or (root.right and root.right.val<= root.val) or not (self.isValidBST(root.left)) or not (self.isValidBST(root.right)):
            return False
        return True
        """