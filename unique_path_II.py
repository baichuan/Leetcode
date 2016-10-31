class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):

        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if obstacleGrid[0][0] == 1:
            return 0;


        row = len(obstacleGrid);
        col = len(obstacleGrid[0]);

        if row > 100 or col > 100:
            return -1;

        optimal_dp = [];

        # initialization step
        for i in range(0, row):

            inner_dp = [];

            for j in range(0, col):
                inner_dp.append(0);
            optimal_dp.append(inner_dp);

        # update first row based on the obstacle

        break_row = -1;

        for c in range(0, col):

            if obstacleGrid[0][c] == 0:
                optimal_dp[0][c] = 1;

            else:

                optimal_dp[0][c] = 0;
                break_row = c;
                break;

        if break_row != -1:
            for c_ in range(break_row+1, col):
                optimal_dp[0][c_] = 0;

        # update first column based on the obstacle
        break_col = -1;
        for r in range(0, row):
            if obstacleGrid[r][0] == 0:
                optimal_dp[r][0] = 1;

            else:

                optimal_dp[r][0] = 0;
                break_col = r;
                break;

        if break_col != -1:

            for r_ in range(break_col+1, row):
                optimal_dp[r_][0] = 0;

        # dynamic programming main loop

        for pos in range(1, row):
            for inpos in range(1, col):
                if obstacleGrid[pos][inpos] != 1:
                    optimal_dp[pos][inpos] = optimal_dp[pos-1][inpos] + optimal_dp[pos][inpos-1];

                else:
                    optimal_dp[pos][inpos] = 0;

        res = optimal_dp[row-1][col-1];

        return res;
