class Solution(object):

    def removeDuplicates(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 2:
            return len(nums);

        j = 1;
        
        for i in range(2, len(nums)):
            
            if nums[i] != nums[j] or nums[i] != nums[j - 1]:
                
                j = j + 1;
                nums[i], nums[j] = nums[j], nums[i];

        return j + 1;
