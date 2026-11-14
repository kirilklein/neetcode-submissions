# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def dfs_compare(rootp, rootq):
            if not rootp and not rootq:
                return True
            if not rootp or not rootq:
                return False
            if rootp.val != rootq.val:
                return False
            return dfs_compare(rootp.left, rootq.left) and dfs_compare(rootp.right, rootq.right)
        
        # go through main tree, check if subroot.val==node.val
        # if so: dfs_compare(). for each compare.
        # probably optimization
        subroot_val = subRoot.val 
        def dfs_traverse(root):
            if not root:
                return False
            if root.val == subroot_val:
                if dfs_compare(root, subRoot):
                    return True
            return dfs_traverse(root.left) or dfs_traverse(root.right)

        return dfs_traverse(root)

        