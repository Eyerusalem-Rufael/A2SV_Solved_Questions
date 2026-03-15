bracket = input().strip()
count = 0
max_length = 0
stk = [-1] #boundary
for idx , val in enumerate(bracket):
    if val == '(':
        stk.append(idx)
    else:
        stk.pop()
        if not stk:
            stk.append(idx) # we got new boundary
        else:
            length = idx - stk[-1] 
            if max_length < length:
                max_length = length
                count = 1 

            elif length == max_length:
                count += 1

if max_length == 0:
    print(0 , 1)
else:
    print(max_length , count)