class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for i in s:
            if i != ']':
                stk.append(i)
            else:
                curr_str = ""
                while stk and stk[-1] != '[':
                    curr_str = stk.pop() + curr_str

                while stk and stk[-1] == '[': 
                     stk.pop()

                digit = ""
                while stk and (stk[-1]).isdigit():
                    digit = stk.pop() + digit
                
                curr_str = curr_str * int(digit)
                stk.append(curr_str)
            
        return ''.join(stk)