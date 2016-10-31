class Solution(object):

    def threeSum(self, nums):

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort();
        res = set();

        if len(nums) < 3:
            return [];

        else:

            for i in range(0, len(nums) - 1):
                j = i + 1;
                k = len(nums) - 1;

                while j < k:
                    sum = nums[i] + nums[j] + nums[k];
                    if sum == 0:
                        res.add((nums[i], nums[j], nums[k]));
                        j = j + 1;
                        k = k - 1;

                    elif sum < 0:
                        j = j + 1;

                    else:
                        k = k - 1;

        return list(res);
