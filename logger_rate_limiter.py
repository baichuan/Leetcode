class Logger(object):

    def __init__(self):

        """
        Initialize your data structure here.
        """

        # build a hash table: key is string and value is time-stamp
        self.dict = {};

    def shouldPrintMessage(self, timestamp, message):

        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """

        if message not in self.dict.keys():

            self.dict[message] = timestamp;
            return True;

        else:
            
            prev_timestamp = self.dict[message];
            if timestamp - prev_timestamp >= 10:
                self.dict[message] = timestamp;
                return True;
            else:
                return False;

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
