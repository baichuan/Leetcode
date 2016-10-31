class Solution(object):

    def threeSumSmaller(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort();

        if len(nums) < 3:
            return 0;

        count = 0;
        for i in range(0, len(nums)-1):
            j = i + 1;
            k = len(nums) - 1;

            while j < k:

                sum = nums[i] + nums[j] + nums[k];

                if sum >= target:
                    k = k - 1;

                elif sum < target:

                    count = count + k - j;
                    j = j + 1;

        return count;
