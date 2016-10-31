class ZigzagIterator(object):

    def __init__(self, v1, v2):

        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """

        # initialize a new python list here

        self.l = [];
        i = 0;

        while i < max(len(v1), len(v2)):
            if i < len(v1):
                self.l.append(v1[i]);
            if i < len(v2):
                self.l.append(v2[i]);
            i = i + 1;

        self.index = 0;

        
    def next(self):

        """
        :rtype: int
        """
        nextEle = self.l[self.index]
        self.index = self.index + 1;
        return nextEle;


    def hasNext(self):

        """
        :rtype: bool
        """

        if self.index < len(self.l):
            return True;

        return False;

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
