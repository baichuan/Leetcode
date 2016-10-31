class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
	
	# time complexity: O(k + n)
	# space complexity: O(1)

        resList = [0]*length;
        for i in range(0, len(updates)):
            startIndex = updates[i][0];
            endIndex = updates[i][1];
            inc = updates[i][2];

            resList[startIndex] = resList[startIndex] + inc;
            if endIndex + 1 < length:
                resList[endIndex + 1] = resList[endIndex + 1] - inc;

        sum = 0;
        for pos in range(0, len(resList)):
            sum = sum + resList[pos];
            resList[pos] = sum;

        return resList;
