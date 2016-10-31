class Solution(object):

    def integerBreak(self, n):

        """
        :type n: int
        :rtype: int
        """

        if n == 2:
            return 1;

        if n == 3:
            return 2;

        if n % 3 == 0:
            return int(math.pow(3, n/3));

        elif n % 3 == 1:
            return int(math.pow(3, (n-4)/3) * 2 * 2);

        else:
            return int(math.pow(3, n/3) * 2);
