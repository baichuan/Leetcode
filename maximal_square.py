class Solution(object):

    def maximalSquare(self, matrix):

        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        # represent C[i][j] as side length of the largest square, where (i, j) block is the bottom-right-most block of that square area
        # DP recursive solution: C[i][j] = min(C[i-1][j], C[i][j-1], C[i-1][j-1]) + 1

        if len(matrix) == 0:
            return 0;

        row = len(matrix);
        col = len(matrix[0]);

#       dp = [[0] * (col + 1)] * (row + 1)

        dp = [];

        for pos in range(0, row + 1):
            inter_dp = [];
            for inpos in range(0, col + 1):
                inter_dp.append(0);
            dp.append(inter_dp);

        # main loop of dynamic programming

        maxSide = 0;
        for i in range(1, row + 1):
            for j in range(1, col + 1):

                if int(matrix[i - 1][j - 1]) == 1:                    

                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1;

                    if dp[i][j] > maxSide:
                        maxSide = dp[i][j];

        return maxSide * maxSide;
