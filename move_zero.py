class Solution(object):

    def moveZeroes(self, nums):

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        count = 0;

        for pos in range(0, len(nums)):
            
            if nums[pos] != 0:
                nums[count] = nums[pos];
                count = count + 1;
                
        while count < len(nums):
            nums[count] = 0;
            count = count+1;
