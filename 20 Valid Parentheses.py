class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        stack = []
        
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if not stack or stack.pop() != mapping[c]:
                    return False

        return not stack
