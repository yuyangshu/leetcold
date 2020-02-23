class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import Counter

        counter = Counter([s[i - 10: i] for i in range(10, len(s) + 1)])

        return [key for key in counter.keys() if counter[key] > 1]
