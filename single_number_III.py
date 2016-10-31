class Solution(object):

    def singleNumber(self, nums):

        """
        :type nums: List[int]
        :rtype: List[int]
        """

        dict = {};

        for i in range(0, len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1

            else:
                dict[nums[i]] += 1

        res_list = [];
        for k, v in dict.items():
            if v == 1:
                res_list.append(k);

            if len(res_list) == 2:
                return res_list;
