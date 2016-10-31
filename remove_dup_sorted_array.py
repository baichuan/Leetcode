class Solution(object):

    def removeDuplicates(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        # two pointers
        
        if nums == []:
            return 0;

        i = 0;
        j = 0;

        for i in range(0, len(nums)):
            
            if nums[i] != nums[j]:

                nums[i], nums[j + 1] =  nums[j + 1], nums[i];
                j = j + 1;

        return j + 1;
