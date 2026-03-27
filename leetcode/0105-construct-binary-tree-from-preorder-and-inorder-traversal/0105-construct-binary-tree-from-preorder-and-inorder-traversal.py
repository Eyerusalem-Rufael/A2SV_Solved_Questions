# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {elt:idx for idx,elt in enumerate(inorder)} #to solit L->R
        self.idx_preorder = 0

        def dfs(left,right):
            if left > right:
                return None

            curr_root_val = preorder[self.idx_preorder]
            self.idx_preorder += 1
            cur_root = TreeNode(curr_root_val)
            mid = inorder_idx[curr_root_val]
            cur_root.left = dfs(left,mid-1) 
            cur_root.right = dfs(mid+1,right) 
            return cur_root

        return dfs(0,len(inorder)-1) 