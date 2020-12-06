class Solution:
    def interpret(self, command: str) -> str:
        return re.sub(r'\(al\)', 'al', re.sub(r'\(\)', 'o', command))
