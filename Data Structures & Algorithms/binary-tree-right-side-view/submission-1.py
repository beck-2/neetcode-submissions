# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res, q = [], deque()
        if root:
            q.append(root)
        while q:
            res.append(q[-1].val) #q[-1] can be accessed O(1) because its a deque
            for _ in range(len(q)): #_ is a throwaway variable name, range only evaluates length of q once even as we're adding nodes to it
                node = q.popleft()
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)
        return res

        """ ts works. now can I do it without level?
        res, q = [], deque()
        if root:
            q.append(root)
        while q:
            level=[]
            while q:
                level.append(q.popleft())
            res.append((level[-1]).val) #last value is rightmost
            for n in level:
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)

        return res
        """



        """ oopps i didn't read the problem lol
        res= [root.val] if root else []
        cur=root
        while cur:
            if cur.right:
                cur=cur.right
                res.append(cur.val)
            elif cur.left:
                cur=cur.left
                res.append(cur.val)
            else:
                return res
        return res
        """