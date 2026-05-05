# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
       self.best = 0
       def dfs(node):
        #basecase
        if not node:
            return True,float('inf'),float('-inf'),0
        is_BST_left,left_min,left_max,left_tot = dfs(node.left)
        is_BST_right,right_min,right_max,right_tot = dfs(node.right)
        if is_BST_left and is_BST_right and left_max < node.val < right_min:
            tot = left_tot + right_tot + node.val
            self.best = max(self.best,tot)
            return True,min(node.val,left_min),max(node.val,right_max),tot

        return False,float('-inf'),float('inf'),0

       dfs(root)
       return self.best