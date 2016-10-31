class HitCounter(object):

    def __init__(self):

        """
        Initialize your data structure here.
        """
        self.dict = {};

    def hit(self, timestamp):

        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """

        if timestamp not in self.dict:
            self.dict[timestamp] = 1;
        else:
            self.dict[timestamp] += 1;


    def getHits(self, timestamp):

        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """

        totalCount = 0;
        for k, v in self.dict.items():
            if timestamp - k < 300:
                totalCount = totalCount + v;
            else:
                del self.dict[k];

        return totalCount;

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
