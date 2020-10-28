class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [1] * (len(s) + 1)
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s) + 1):
            if s[i - 1] == '0':
                dp[i] = dp[i - 2] if s[i - 2] in {'1', '2'} else 0
            elif '1' <= s[i - 1] <= '6' and s[i - 2] in {'1', '2'}:
                dp[i] = dp[i - 2] + dp[i - 1]
            else:
                dp[i] = dp[i - 1] + (dp[i - 2] if s[i - 2] == '1' else 0)

        return dp[-1]
