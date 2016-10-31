class Solution(object):

    def searchRange(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 0:
            return [-1, -1];

        left = 0;
        right = len(nums) - 1;
        start_index = -1;
        end_index = -1;

        # finding start_index
        while left <= right:

            mid = (left + right) / 2;
            if nums[mid] == target and (mid == 0 or nums[mid-1] < target):
                start_index = mid;
                break;

            elif nums[mid] < target:
                left = mid + 1;

            else:
                right = mid - 1;

        # finding end_index
        left = 0;
        right = len(nums) - 1;
        while left <= right:
            mid = (left + right) / 2;
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid+1] > target):
                end_index = mid;
                break;

            elif nums[mid] <= target:
                left = mid + 1;

            else:
                right = mid - 1;

        return [start_index, end_index];
