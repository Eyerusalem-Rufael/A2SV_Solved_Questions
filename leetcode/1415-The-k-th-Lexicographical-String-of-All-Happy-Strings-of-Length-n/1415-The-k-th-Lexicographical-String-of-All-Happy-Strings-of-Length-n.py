class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def back(curr):
            if len(res) == k:
                return True
            if len(curr) == n:
                res.append(curr)
                return len(res) == k

            for i in ['a','b','c']:
                if not curr or curr[-1] != i:
                    if back(curr + i):
                        return True
            return False

        back("")

        return res[k-1] if len(res) >= k else ""