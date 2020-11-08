class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import Counter

        n, result = len(s), 0
        frequencies = [item[1] for item in Counter(s).most_common()]

        start, available = 0, None
        while start < n - 1:
            for i in range(start, len(frequencies) - 1):
                if frequencies[i] == frequencies[i + 1]:
                    if available is None:
                        available = set(range(1, frequencies[i])) - set(frequencies[i + 1:])
                    break
            else:
                return result

            available &= set(range(1, frequencies[i]))
            if len(available) > 0:
                result += frequencies[i] - max(available)
                available.remove(max(available))
            else:
                result += frequencies[i]

            start = i + 1
        else:
            return result
