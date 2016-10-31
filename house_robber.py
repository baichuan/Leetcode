class Solution(object):

    def rob(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        # dp(i) = max{nums[i]+dp[i-2], dp[i-1]}

        if len(nums) == 0:
            return 0;

        if len(nums) == 1:
            return nums[0];

        if len(nums) == 2:
            return max(nums[0], nums[1]);

            
        dp = [0]*len(nums);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1]);

        return dp[-1];


# use rolling array to save space complexity

class Solution(object):

    def rob(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        # use rolling array in order to save space complexity O(1)

        if len(nums) == 0:
            return 0;

        if len(nums) == 1:
            
            return nums[0];

            
        if len(nums) == 2:

            return max(nums[0], nums[1]);


        nums[1] = max(nums[0], nums[1]);
        
        for i in range(2, len(nums)):
            
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1]);

        return nums[i];
