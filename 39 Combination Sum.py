class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        from collections import defaultdict

        filtered = sorted([item for item in candidates if item <= target])

        combinations = defaultdict(list)
        for item in filtered:
            combinations[item].append([item])
        
        if filtered:
            for _ in range(target // filtered[0] + 1):
                new_entries = defaultdict(list)
                for item in filtered:
                    for listsum in sorted(combinations.keys()):
                        if item + listsum <= target:
                            new_entries[item + listsum] += [sorted(x + [item]) for x in combinations[listsum]]
                        else:
                            break

                for key in new_entries.keys():
                    for item in new_entries[key]:
                        if item not in combinations[key]:
                            combinations[key].append(item)

        return combinations[target]
