class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        remaining = set(range(n)) - {headID}
        
        while remaining:
            current_inform_time = informTime.copy()
            current_manager = manager.copy()

            for i in frozenset(remaining):
                mgr = current_manager[i]

                if mgr >= 0:
                    informTime[i] += current_inform_time[mgr]
                    manager[i] = current_manager[mgr]
                else:
                    remaining.remove(i)

        return max(informTime)
