class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i for i in range(1, m + 1)]
        results = []

        for q in queries:
            result = P.index(q)
            results.append(result)
            P = [q] + P[:result] + (P[result + 1:] if result < m - 1 else [])

        return results
