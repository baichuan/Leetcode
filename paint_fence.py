class Solution(object):

    def numWays(self, n, k):

        """
        :type n: int
        :type k: int
        :rtype: int
        """

        # dp[i] represents total number of ways you can paint up to i-th fence
        # dp[i] = (k-1)*dp[i-2] + (k-1)*dp[i-1]

        if n == 0:
            return 0;

        elif n == 1:
            return k;

        elif n == 2:
            return k*k;

        dp = [0]*n;
        dp[0] = k;
        dp[1] = k*k;

        for i in range(2, n):
            dp[i] = (k-1)*dp[i-2] + (k-1)*dp[i-1];

        return dp[n-1];
