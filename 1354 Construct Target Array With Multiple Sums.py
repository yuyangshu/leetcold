class Solution:
    def isPossible(self, target: List[int]) -> bool:
        import heapq

        # heap = heapq.heapify([-item for item in target]) does not work
        heap = []
        for item in target:
            heapq.heappush(heap, -item)

        current = -heapq.heappop(heap)
        total = -sum(heap)

        while current != 1:
            if current <= total or not total:
                return False
            previous = -(current % total)

            current = -heapq.heappushpop(heap, previous)
            total -= current + previous

        return True
