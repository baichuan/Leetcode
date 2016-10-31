class Solution(object):

    def majorityElement(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 3:
            return nums[0];

            
        temp1 = self.majorityElement(nums[0:len(nums)/2]);
        temp2 = self.majorityElement(nums[len(nums)/2:]);
        
        if temp1 == temp2:
            return temp1;

        else:
            count1 = 0;
            count2 = 0;

            for i in range(0, len(nums)):
                if nums[i] == temp1:
                    count1 = count1 + 1;

                if nums[i] == temp2:
                    count2 = count2 + 1;

            if count1 > len(nums)/2:
                return temp1;

            elif count2 > len(nums)/2:
                return temp2;

            else:
                return -1;
