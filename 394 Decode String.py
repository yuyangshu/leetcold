class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                pattern, repetition = '', ''

                while stack[-1] != '[':
                    pattern = stack.pop() + pattern
                stack.pop()
                while stack and stack[-1].isdigit():
                    repetition = stack.pop() + repetition
                
                stack.append(pattern * int(repetition))
            else:
                stack.append(c)
                
        return "".join(stack)
