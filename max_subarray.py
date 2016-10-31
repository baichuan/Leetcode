class Solution(object):

    def maxSubArray(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        # use dynamic programming to solve the problem
	# As we use dp based approach, so it can handle streaming data (LinkedIn followup)

        # prefixSum(i), which is sum of max sub-array which ends at index i
        # prefixSum(i) = A[i] if i = 1 or max(A[i], prefixSum(i-1) + A[i] otherwise)

	# keep track of this example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] => [4, -1, 2, 1]

        if len(nums) == 1:
            return nums[0];

        prefix_sum = nums[0];
        start_index = 0;
        end_index = 0;
        max_sum = nums[0];

        for i in range(1, len(nums)):

            if nums[i] > prefix_sum + nums[i]:
                prefix_sum = nums[i];
                start_index = i;

            else:
                prefix_sum = prefix_sum + nums[i];

            if max_sum < prefix_sum:
                max_sum = prefix_sum;
                end_index = i;

        return max_sum;
