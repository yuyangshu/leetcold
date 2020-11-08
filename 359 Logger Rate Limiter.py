class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.last_seen = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        last_seen = self.last_seen.get(message, None)

        if last_seen is not None and last_seen > timestamp - 10:
            return False
        else:
            self.last_seen[message] = timestamp
            return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)