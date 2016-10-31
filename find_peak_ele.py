class Solution:

    # @param nums, an integer[]
    # @return an integer

    def findPeakElement(self, nums):

	# [1, 3, 20, 4, 1, 0, 7]
        left = 0;
        right = len(nums) - 1;

        while left < right:

            mid = (left + right) / 2;
            if nums[mid] > nums[mid + 1]:
                right = mid;

            else:
                left = mid + 1;

        return left;
