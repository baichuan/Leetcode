class Solution(object):

    def minSubArrayLen(self, s, nums):

        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        start = 0;
        end = 0;
        sum = 0;

        minLength = sys.maxint;

        while end < len(nums):

            sum = sum + nums[end];
            end = end + 1;

            while sum >= s:
                minLength = min(minLength, end - start);
                sum = sum - nums[start];
                start = start + 1;

        if minLength == sys.maxint:
            return 0;

        else:
            return minLength;
