class Solution(object):

    def wiggleSort(self, nums):

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        for i in range(0, len(nums) - 1):
            if i % 2 == 0:
                if nums[i] > nums[i+1]:
                    # switch these two numbers
                    nums[i], nums[i+1] = nums[i+1], nums[i];

            elif i % 2 == 1:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i];
