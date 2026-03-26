class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def dfs(s):
            if not s:
                return ""

            unique = set(s)
            for idx , elt in enumerate(s):
                if elt.swapcase() not in unique:
                    left = dfs(s[:idx])
                    right = dfs(s[idx+1:])

                    if len(left) >= len(right):
                        return left
                    else:
                        return right
                    
            return s

        return dfs(s)