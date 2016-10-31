class Solution(object):

    def threeSumClosest(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort();
        min_diff = 100000;
        res = 0;

        for i in range(0, len(nums) - 1):
            j = i + 1;
            k = len(nums) - 1;

            while j < k:
                sum = nums[i] + nums[j] + nums[k];
                diff = abs(sum - target);

                if diff < min_diff:
                    min_diff = diff;
                    res = sum;

                if sum == target:
                    return sum;

                elif sum < target:
                    j = j + 1;

                else:
                    k = k - 1;

        return res;
