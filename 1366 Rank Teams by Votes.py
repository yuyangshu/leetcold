class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        from collections import Counter

        results = sorted(votes[0])
        for i in range(len(votes[0]) - 1, -1, -1):
            results.sort(key=lambda x: Counter([vote[i] for vote in votes])[x], reverse=True)

        return "".join(results)
