class Solution(object):

    def sortTransformedArray(self, nums, a, b, c):

        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """

        # if a > 0, then max value in either end
        # if a < 0, then min value in either end
        # so use two pointer idea

        ret = []
        l = 0
        r = len(nums)-1

        while l <= r:
            n_l = a*nums[l]**2 + b*nums[l] + c
            n_r = a*nums[r]**2 + b*nums[r] + c

            if a >= 0:

                if n_l >= n_r:
                    ret.append(n_l)
                    l += 1
                else:
                    ret.append(n_r)
                    r -= 1

            else:
                if n_l < n_r:
                    ret.append(n_l)
                    l += 1
                else:
                    ret.append(n_r)
                    r -= 1

        if a >= 0:
            return ret[::-1]

        return ret
