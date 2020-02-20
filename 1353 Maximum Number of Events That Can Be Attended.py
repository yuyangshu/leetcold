class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key=lambda x: (x[1], x[0]))

        days = set()

        for event in events:
            for i in range(event[0], event[1] + 1):
                if i not in days:
                    days.add(i)
                    break

        return len(days)
