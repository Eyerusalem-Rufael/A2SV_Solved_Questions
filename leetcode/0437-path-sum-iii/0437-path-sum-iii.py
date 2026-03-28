# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pre_sum = defaultdict(int)
        pre_sum[0] = 1

        def dfs(node,cur_sum):
            if not node:
                return 0

            cur_sum += node.val
            count = pre_sum[cur_sum - targetSum]

            pre_sum[cur_sum] += 1
            count += dfs(node.left,cur_sum)
            count += dfs(node.right,cur_sum)
            pre_sum[cur_sum] -= 1 #remove the sum 

            return count

        return dfs(root,0) #node,cur_sum