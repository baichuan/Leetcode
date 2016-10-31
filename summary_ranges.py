class Solution(object):

    def summaryRanges(self, nums):

        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if nums == []:
            return [];

        resList = [];
        start = nums[0];
        end = nums[0];

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                end = nums[i];

            else:
                resList.append(self.getStr(start, end));
                start = nums[i];
                end = nums[i];

        resList.append(self.getStr(start, end));

        return resList;

        
    def getStr(self, start, end):
        if start == end:
            return str(start);

        else:
            return str(start) + "->" + str(end);
