class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        results = defaultdict(list)
        for item in strs:
            results[str(sorted(item))].append(item)

        return [results[key] for key in results.keys()]
