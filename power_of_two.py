class Solution(object):

    def isPowerOfTwo(self, n):

        """
        :type n: int
        :rtype: bool
        """

	# power of 2 means only one bit of n is "1", so use the trick n&(n - 1) to judge whether that is the case

        if n <= 0:
            return False;
        else:
            return not (n & (n-1));
