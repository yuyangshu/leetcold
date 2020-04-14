class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def get_prohibited(array):
            return array[-1] if len(array) > 1 and array[-1] == array[-2] else ''

        def get_next(dictionary, last):
            for key in sorted(dictionary.keys(), key=dictionary.get, reverse=True):
                if key != last and dictionary[key] > 0:
                    return key

        pool = {
            'a': a,
            'b': b,
            'c': c
        }

        results = []

        for _ in range(a + b + c):
            prohibited = get_prohibited(results)
            next_char = get_next(pool, prohibited)

            if next_char:
                results.append(next_char)
                pool[next_char] -= 1

        return ''.join(results)
