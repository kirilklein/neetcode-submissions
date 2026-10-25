class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            ')': '(', 
            '}': '{', 
            ']': '['
            }
        closing = set(lookup.keys())
        opening = set(lookup.values())
        stack = []
        for c in s:
            if c in closing:
                if len(stack)==0:
                    return False
                elif lookup[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack)==0:
            return True
        return False