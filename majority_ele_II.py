class Solution(object):

    def majorityElement(self, nums):

        """
        :type nums: List[int]
        :rtype: List[int]
        """

        dict = {};

        for i in range(0,len(nums)):
            if dict.get(nums[i], -1) == -1:
                count = 0;
                count = count + 1;
                dict[nums[i]] = count;

            else:
                count = dict[nums[i]];
                count = count + 1;
                dict[nums[i]] = count;

        res = [];   
        for k, v in dict.items():
            if v > int(len(nums)/3):
                res.append(k);

        return res;
