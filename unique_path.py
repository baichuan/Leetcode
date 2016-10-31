class Solution(object):

    def uniquePaths(self, m, n):

        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # dp[i][j]: at position (i, j), the total number of paths
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]

        if m > 100 or n > 100:
            return -1;

        dp = [];

        for i in range(0, m):

            inter_dp = [];

            for j in range(0, n):

                if i == 0 or j == 0:
                    inter_dp.append(1);

                else:
                    inter_dp.append(0);

            dp.append(inter_dp);

        for pos in range(1, m):
            for inpos in range(1, n):
                dp[pos][inpos] = dp[pos-1][inpos] + dp[pos][inpos-1];

        return dp[m-1][n-1];
