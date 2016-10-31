class Solution(object):

    def myPow(self, x, n):

        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # use divide and conquer and time complexity is O(lgn)

        if n == 0:

            return 1;

        elif n < 0:

            return 1 / self.myPow(x, -n);

        elif n % 2 == 0:

            v = self.myPow(x, n/2);

            return v*v;

        else:

            v = self.myPow(x, (n-1)/2);

            return v*v*x;
