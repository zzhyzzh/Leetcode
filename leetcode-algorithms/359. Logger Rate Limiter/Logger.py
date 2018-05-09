class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_table = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if self.time_table.get(message, -1) >= 0 \
            and timestamp - self.time_table[message] < 10:
                return False
        else:
            self.time_table[message] = timestamp
            return True

# Your Logger object will be instantiated and called as such:
obj = Logger()
param_1 = obj.shouldPrintMessage(1, "foo")
print(param_1)
param_1 = obj.shouldPrintMessage(2,"bar")
print(param_1)
param_1 = obj.shouldPrintMessage(3,"foo")
print(param_1)
param_1 = obj.shouldPrintMessage(8,"bar")
print(param_1)
param_1 = obj.shouldPrintMessage(10,"foo")
print(param_1)
param_1 = obj.shouldPrintMessage(11,"foo")
print(param_1)
