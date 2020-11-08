class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        import re

        whole_text = '\n'.join(source)
        replaced = re.sub("//.*|/\*(.|\n)*?\*/", "", whole_text).split('\n')
        return [s for s in replaced if s]
