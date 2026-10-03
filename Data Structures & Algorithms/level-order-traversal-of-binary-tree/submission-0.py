# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = [root] if root else []
        while level:
            res.append([n.val for n in level])
            level = [c for n in level for c in (n.left, n.right) if c]
        return res
        
        """
        if root is None:
            return []
        res, q= [], deque()
        q.append(root)
        while q:
            level=[]
            for _ in range(len(q)):
                node=q.popleft
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        return res



        
        #instead of using a deque we can just use the list itself??
        #But how do i avoid a nested loop? 
        if root:
            res=[[root]]
        else:
            return [[]]
        for l in res:
            cur=[]
            for node in l:
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            res.append(cur)
        """






