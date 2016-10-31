class Solution(object):

    def sortColors(self, nums):

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # counting sort
        
        red_count = 0;
        white_count = 0;
        blue_count = 0;

        for i in range(0, len(nums)):
            
            if nums[i] == 0:
                red_count += 1;

            elif nums[i] == 1:
                white_count += 1;

            else:
                blue_count += 1;

        for pos in range(0, red_count):
            nums[pos] = 0;

        for pos in range(red_count, red_count + white_count):
            nums[pos] = 1;

        for pos in range(red_count + white_count, red_count + white_count + blue_count):
            nums[pos] = 2;


class Solution(object):

    def sortColors(self, nums):

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # two pointers
        
        red_index = 0;
        blue_index = len(nums) - 1;

        i = 0;
        
        while i <= blue_index:
            
            if nums[i] == 0:    

                # swap nums[i] and nums[red_index]

                nums[i], nums[red_index] = nums[red_index], nums[i];
                red_index += 1;
                i = i + 1;

            elif nums[i] == 2:
                
                # swap nums[i] and nums[blue_index]
                
                nums[i], nums[blue_index] = nums[blue_index], nums[i];
                blue_index -= 1;

            else:

                i = i + 1;
