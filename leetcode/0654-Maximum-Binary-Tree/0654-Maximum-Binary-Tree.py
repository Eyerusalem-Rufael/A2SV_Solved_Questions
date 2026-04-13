# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums):
            if not nums:
                return  None

            max_idx = nums.index(max(nums))
            node = TreeNode(nums[max_idx])
            node.left = dfs(nums[:max_idx])
            node.right = dfs(nums[max_idx+1:])
            return node

        return dfs(nums)