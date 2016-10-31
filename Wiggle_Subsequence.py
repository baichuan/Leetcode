class Solution(object):

    def wiggleMaxLength(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        ret = len(nums)
        prevDiff = None
        for i in range(1, len(nums)):
            curDiff = nums[i] - nums[i - 1]
            if curDiff == 0:
                ret -= 1
                continue
            if prevDiff is not None:
                if curDiff > 0 and prevDiff > 0:
                    ret -= 1
                elif curDiff < 0 and prevDiff < 0:
                    ret -= 1
            prevDiff = curDiff
        return ret
