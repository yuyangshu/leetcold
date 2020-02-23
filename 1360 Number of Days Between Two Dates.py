class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        from datetime import datetime
        
        return abs((datetime.fromisoformat(date1) - datetime.fromisoformat(date2)).days)
