class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0] #act as a base element
        for i in s:
            if i == '(':
                stk.append(0)
            else:
                pop = stk.pop()
                stk[-1] += max(2 * pop , 1)
        return stk[0]