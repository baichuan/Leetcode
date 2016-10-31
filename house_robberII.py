class Solution(object):

    def rob(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0;

        if len(nums) == 1:
            return nums[0];

        if len(nums) == 2:
            return max(nums[0], nums[1]);

        dp1 = [0] * len(nums);
        res1 = 0;
        res2 = 0;

        # don't steal first house and you can steal last house
        dp1[1] = nums[1];

        for i in range(2, len(nums)):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1]);

        res1 = dp1[-1];

        # if steal first house, then you cannot steal last house
        dp2 = [0]*len(nums);

        dp2[0] = nums[0];
        dp2[1] = nums[0];

        for i in range(2, len(nums) -1):
            dp2[i] = max(dp2[i-2] + nums[i], dp2[i-1]);
        res2 = dp2[-2];

        return max(res1, res2);
