class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        A = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:
                if i > len(word) - 2 and s[i - len(word) + 1: i + 1] == word and (i + 1 == len(word) or A[i - len(word)]):
                    A[i] = True

        return A[-1]
