class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        
        counter = Counter(nums)
        return sorted(counter, key=lambda x: counter[x], reverse=True)[:k]
