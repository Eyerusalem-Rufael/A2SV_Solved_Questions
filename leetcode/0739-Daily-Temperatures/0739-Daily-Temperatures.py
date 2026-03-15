class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stk = []

        for idx , elt in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < elt: #monodecr if the top smaller pop it
                popped = stk.pop()
                res[popped] = idx - popped
            stk.append(idx)

        return res