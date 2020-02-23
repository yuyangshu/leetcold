class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        from collections import defaultdict

        mapping = defaultdict(set)
        for i in range(len(s)):
            mapping[s[i]].add(t[i])

        all_values = set()
        for value in mapping.values():
            all_values |= value
        return len(mapping.keys()) == len(all_values) == sum([len(value) for value in mapping.values()])
