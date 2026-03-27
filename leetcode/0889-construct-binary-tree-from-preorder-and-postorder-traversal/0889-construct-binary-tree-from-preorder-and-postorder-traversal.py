# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder_idx = {elt:idx for idx,elt in enumerate(postorder)} #to solit L->R
        self.idx_preorder = 0

        def dfs(left,right):
            if left > right:
                return None

            curr_root_val = preorder[self.idx_preorder]
            cur_root = TreeNode(curr_root_val)
            self.idx_preorder += 1
            
            if left == right:
                return cur_root
            next_left = preorder[self.idx_preorder] #to get the left-subtree

            mid = postorder_idx[next_left]
            cur_root.left = dfs(left,mid) 
            cur_root.right = dfs(mid+1,right-1)  

            return cur_root

        return dfs(0,len(postorder)-1) 