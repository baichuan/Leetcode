class Solution(object):

    def getRow(self, rowIndex):

        """
        :type rowIndex: int
        :rtype: List[int]
        """

	# 一行一行往下算 下一行只根据上一行，只需要保存上一行的值就可以
	# 滚动数组原理

        resList = [];
        resList.append(1);

        if rowIndex == 0:
            return resList;

        for i in range(0, rowIndex):

            resList.insert(0, 1);

            for j in range(1, len(resList) - 1):
                resList[j] = resList[j] + resList[j+1];

        return resList;
