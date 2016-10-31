class Solution(object):

    def findMissingRanges(self, nums, lower, upper):

        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        res = [];

        if nums == []:
            if lower == upper:
                res.append(str(lower));

            else:
                res.append(str(lower) + "->" + str(upper));

            return res;

            
        for i in range(0, len(nums)):
            if i == 0:
                if nums[0] - lower > 0:
                    if nums[0] - lower== 1:
                        res.append(str(lower));

                    else:
                        res.append(str(lower) + "->" + str(nums[0] - 1));

            else:

                if nums[i] - nums[i-1] == 2:
                    res.append(str(nums[i] - 1));

                elif nums[i] - nums[i-1] > 2:
                    res.append(str(nums[i-1] + 1) + "->" + str(nums[i]-1));

        if upper - nums[-1] == 1:
            res.append(str(upper));

        elif upper - nums[-1] > 1:
            res.append(str(nums[-1] + 1) + "->" + str(upper));

        return res;
