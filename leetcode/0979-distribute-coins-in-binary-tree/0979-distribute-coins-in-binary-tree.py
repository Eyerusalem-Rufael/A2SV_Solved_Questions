# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return [0 , 0]
            left_size , left_coin = dfs(node.left)
            right_size , right_coin = dfs(node.right)

            coin = left_coin + right_coin + node.val
            size = left_size + right_size + 1
            self.res += abs(coin -size) 
            return [size,coin]
        dfs(root)
        return self.res

        # self.moves = 0
        # def dfs(node):
        #     if not node:
        #         return 0
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     self.moves += abs(left) + abs(right)

        #     return (node.val - 1) + left + right

        # dfs(root)
        # return self.moves