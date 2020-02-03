class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def recur(previous: List[int], candidates: set, results: List[List[int]]) -> None:
                if len(candidates) == 1:
                    results.append(previous + list(candidates))
                else:
                    for i in candidates:
                        recur(previous + [i], candidates - {i}, results)

        def permute(self, nums: List[int]) -> List[List[int]]:
            results = []
            if nums:
                recur([], set(nums), results)

            return results

        unique_results = []
        recur([], set(range(len(nums))), unique_results)

        results = set()
        for item in unique_results:
            results.add(tuple([nums[x] for x in item]))

        return results
