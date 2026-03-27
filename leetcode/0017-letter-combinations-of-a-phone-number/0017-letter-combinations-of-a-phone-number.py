class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or digits == '1' :
            return []
        arr = []
        comb = []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv','9':'wxyz'}
        def pair(num):

            if len(comb) == len(digits):
                arr.append("".join(comb))
                return 

            for i in mapping[digits[num]]:
                comb.append(i)
                pair(num+1)
                comb.pop()

        pair(0)
        return arr