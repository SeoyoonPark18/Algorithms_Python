#Seoyoon Park

match_dict = {']':'[', '}': '{', ')': '('}

def isValid(s):
    stack =[]
    for char in s:
        if char in ('(' ,'{' ,'['):
            stack.append(char)
        elif char in (')' ,'}' ,']'):
            if not stack or stack[len(stack)-1] != match_dict[char]:
                return False
            stack.pop()

    if stack:
        return False
    else:
        return True
            
   


print(isValid(input()))
