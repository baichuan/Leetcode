class Solution(object):

    def maxSubArrayLen(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # in hash map, key is the sum until ith index, and value is ith index
        sum = 0;
        maxL = 0;
        dict = {};

        for i in range(0, len(nums)):

            sum = sum + nums[i];
            if sum == k:
                maxL = i + 1;
            elif sum - k in dict:
                maxL = max(i - dict[sum-k], maxL);
            if sum not in dict:
                dict[sum] = i;

        return maxL;
