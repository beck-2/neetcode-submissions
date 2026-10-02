# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #vals are unique
        #i wish i could go upwards bro wth
        #use dfs like i guess?
        if p.val==q.val:
            return p
        if (p.val < root.val and q.val> root.val) or (p.val>root.val and q.val<root.val) or p.val==root.val or q.val==root.val:
            return root
        elif p.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)