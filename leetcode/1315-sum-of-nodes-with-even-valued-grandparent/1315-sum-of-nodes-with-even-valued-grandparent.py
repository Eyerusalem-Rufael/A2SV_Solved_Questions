# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(child,parent,g_parent):
            if not child:
                return 0

            total = 0
            if g_parent % 2 == 0:
                total += child.val
                
            total += dfs(child.left,child.val,parent)
            total += dfs(child.right,child.val,parent)
            return total

        return dfs(root,-1,-1)