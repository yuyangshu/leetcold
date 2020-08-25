class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def construct(previous, nexts, results):
            if nexts:
                for char in mappings[nexts[0]]:
                    construct(previous + char, nexts[1:], results)
            else:
                if previous:
                    results.append(previous)

        results = []
        construct("", digits, results)

        return results
