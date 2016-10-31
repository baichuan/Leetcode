class Solution(object):

    def isStrobogrammatic(self, num):

        """
        :type num: str
        :rtype: bool
        """

        # build the the mapping correspondence of numbers using hash table
        mapDict = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'};

        low = 0;
        high = len(num) - 1;

        while low <= high:
            if num[low] in mapDict and num[high] in mapDict:
                if num[low] == mapDict[num[high]] and num[high] == mapDict[num[low]]:
                    low = low + 1;
                    high = high - 1;

                else: 
			return False;

            else:
                return False;

        return True;
