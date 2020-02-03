class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def recur(previous: List[int], candidates: set, results: List[List[int]]) -> None:
            if len(candidates) == 1:
                results.append(previous + list(candidates))
            else:
                for i in candidates:
                    recur(previous + [i], candidates - {i}, results)

        results = []
        if nums:
            recur([], set(nums), results)

        return results
