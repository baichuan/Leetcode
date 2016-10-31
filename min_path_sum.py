class Solution(object):

    def minPathSum(self, grid):

        """
        :type grid: List[List[int]]
        :rtype: int
        """

        dp_sum = [];
        row = len(grid);
        col = len(grid[0]);

        for i in range(0, row):

            inter_dp = [];
            for j in range(0, col):
                inter_dp.append(0);

            dp_sum.append(inter_dp);

        dp_sum[0][0] = grid[0][0];

        # initialize the first row and first column

        for pos in range(1, col):
            dp_sum[0][pos] = dp_sum[0][pos-1] + grid[0][pos];

        for pos in range(1, row):
            dp_sum[pos][0] = dp_sum[pos-1][0] + grid[pos][0];


        # main dp loop        

        for i in range(1, row):
            for j in range(1, col):
                dp_sum[i][j] = min(dp_sum[i-1][j], dp_sum[i][j-1]) + grid[i][j];

        return dp_sum[row - 1][col - 1];
