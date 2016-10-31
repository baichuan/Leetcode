class Solution(object):

    def search(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        start = 0;
        end = len(nums) - 1;

        while start <= end:

            mid = (start + end) / 2;
            if nums[mid] == target:
                return True;

            elif nums[mid] < nums[end]:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1;

                else:
                    end = mid - 1;

            elif nums[mid] > nums[end]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1;

                else:
                    start = mid + 1;

            elif nums[mid] == nums[end]:
                end = end - 1;

        return False;
