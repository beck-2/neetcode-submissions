# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #iterative optimal dfs
        stack, curr= [], root
        while stack or curr:
            while curr: #traverse leftwards to get min
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            k-=1
            if k==0:
                return curr.val
            curr=curr.right


        """
        #genuinely can we use a binary search? k is a const so we can just find smallest val and somehow iterate backwards..... hrm
        #don't have to check whether k is valid thankfully
        #we're also only given the root... like can we manipulate the array itself?
        #can we keep a pointer k values behind the min? and we start walking it towards the right if the left subtree aint big enough?
        #or lowkey just cache the last k values??
        #we can also just do a bst for the min element k times and remove it lol
        #inorder traversal with dfs, stop once we visit kth smallest
        if not root:
            return -1
        res=root.val
        count=k
        def dfs(node):
            nonlocal count, res
            if not node:
                return
            dfs(node.left)
            if count ==0:
                return
            count -=1
            if count==0:
                res=node.val
                return
            dfs(node.right)
        dfs(root)
        return res

            


        
    #lowkey i thought about doing the iterative dfs version with an explicit stack and k-=1
        def dfs(node, x: Optional[TreeNode], int) -> int:
            #find the min and then backtrack! pop k values off the stack (maybe we should use explicit stack instead of recursion?)
            if not root:
                return -1
        """


        