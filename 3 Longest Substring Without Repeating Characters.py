class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = dict()
        max_length = 0
        watermark = -1

        for i in range(len(s)):
            if s[i] in last_seen:
                watermark = max(watermark, last_seen[s[i]])

            max_length = max(max_length, i - watermark)
            last_seen[s[i]] = i

        return max_length
