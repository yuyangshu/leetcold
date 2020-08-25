class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        
        maximum = 0
        heapq.heapify(intervals)
        current_pool = []
        
        while intervals:
            meeting = heapq.heappop(intervals)
            
            current = meeting[0]
            heapq.heappush(current_pool, meeting[1])
            
            while current_pool and current_pool[0] <= current:
                heapq.heappop(current_pool)
            else:
                maximum = max(maximum, len(current_pool))

        return maximum
