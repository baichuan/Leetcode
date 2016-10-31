class Solution(object):

    def singleNumber(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        dict = {};
        for pos in range(0, len(nums)):
            if dict.get(nums[pos], -1) == -1:
                count = 0;
                count = count + 1;
                dict[nums[pos]] = count;

            else:
                count = dict[nums[pos]];
                count = count +1;
                dict[nums[pos]] = count;

        for k, v in dict.items():
            if v != 2:
                return k;


class Solution(object):

    def singleNumber(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0;
        for i in range(0, len(nums)):
            res = res ^ nums[i];
        return res;
