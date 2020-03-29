class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter

        counter = Counter(arr)
        results = {key for key in counter if key == counter[key]}
