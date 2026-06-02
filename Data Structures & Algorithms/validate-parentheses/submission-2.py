class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char not in ['(', ')', '{', '}', '[', ']']:
                continue
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if char == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                if char == "]":
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
