# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(qroot, proot):
            if not qroot and not proot:
                return True
            if not qroot or not proot:
                return False
            if qroot.val != proot.val:
                return False
            
            return dfs(qroot.left, proot.left) and dfs(qroot.right, proot.right)
        return dfs(q, p)

        