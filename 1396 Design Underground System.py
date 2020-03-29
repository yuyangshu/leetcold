class UndergroundSystem:

    def __init__(self):
        from collections import defaultdict
        from statistics import mean

        self._checkins = {}
        self._completed = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self._checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self._checkins.pop(id)
        self._completed[(start_station, stationName)].append(t - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return mean(self._completed[(startStation, endStation)])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
