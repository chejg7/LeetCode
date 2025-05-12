class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in pair.values():
                stack.append(char)
            elif char in pair:
                if len(stack) > 0 and pair[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
            
        return not stack
