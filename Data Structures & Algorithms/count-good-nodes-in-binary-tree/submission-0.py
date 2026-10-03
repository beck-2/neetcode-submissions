# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #1:29
        #have each node's value track the max it's seen so far
        if root is None:
            return 0
        res, q = 1, deque() # the root, if it exists, must be good
        q.append(root)
        while q:
            n=q.popleft()
            if n.left:
                if (n.left.val>=n.val): res +=1
                else: n.left.val=n.val # trickle down larger val
                q.append(n.left)
            if n.right:
                if (n.right.val>=n.val): res +=1
                else: n.right.val=n.val # trickle down larger val
                q.append(n.right)
        return res

        