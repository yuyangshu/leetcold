class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s

        maximum = s[0]

        for i in range(len(s)):
            for l in (i - 1, i):
                r = i + 1

                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r - l + 1 > len(maximum):
                        maximum = s[l : r + 1]

                    l -= 1
                    r += 1

        return maximum
