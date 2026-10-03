# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #3:01
        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right) #postorder
            balanced=left[0] and right[0] and abs(left[1]-right[1]) <=1 #returning a tuple of bool, int to represent truth and height
            return [balanced, 1+max(left[1], right[1])]
        return dfs(root)[0] #return just the bool
        

        """
        return abs(height(root.left)-height(root.right)) <=1 #difference between height of left and right subtrees cant be more than one

        #postorder dfs... completeness and balance are 2 dif things
        def height(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            
        if root is None:
            return True 
        return height(root.left)==height(root.right)
"""