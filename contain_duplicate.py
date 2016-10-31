class Solution(object):

    def containsDuplicate(self, nums):

        """
        :type nums: List[int]
        :rtype: bool
        """

        dict = {};
        for i in range(0, len(nums)):
            if nums[i] not in dict:

                dict[nums[i]] = 1;

            else:

                dict[nums[i]] += dict[nums[i]];

                
        for v in dict.values():
            if v >= 2:
                return True;
        return False;
