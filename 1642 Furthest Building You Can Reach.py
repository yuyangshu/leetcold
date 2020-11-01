class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        import heapq
        
        n = len(heights)
        costs = [0] + [max(heights[i] - heights[i - 1], 0) for i in range(1, n)]
        heap = []

        for i in range(n):
            bricks -= costs[i]
            heapq.heappush(heap, -costs[i])

            if bricks < 0:
                if ladders > 0:
                    ladders -= 1
                    bricks -= heapq.heappop(heap)
                else:
                    return i - 1

        return n - 1
