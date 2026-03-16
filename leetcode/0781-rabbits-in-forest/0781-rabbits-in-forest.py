class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for key , val in count.items():
            group = key + 1
            groups = ceil(val / group)
            ans += group *groups
        return ans
