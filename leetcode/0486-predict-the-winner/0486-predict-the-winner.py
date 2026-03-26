class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        n = len(nums) - 1

        def predict(left,right):
            if left == right: #base-case
                return nums[left]

            if (left,right) in memo:
                return memo[(left,right)] #avoid redundant calculation

            pick_left = nums[left] - predict(left+1,right)
            pick_right = nums[right] - predict(left,right-1)
            memo[(left,right)] = max(pick_left,pick_right)

            return memo[(left,right)]

        return predict(0,n) >= 0 #if the score is + player1 is gonna win

    