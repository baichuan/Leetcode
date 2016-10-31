class NumMatrix(object):

    def __init__(self, matrix):

        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """

        self.copyMatrix = matrix;
        self.sumMatrix = [];

        if matrix != []:
            row = len(matrix);
            col = len(matrix[0]);

            for i in range(0, row):
                temp = [];
                for j in range(0, col):
                    temp.append(0);
                self.sumMatrix.append(temp);

            rowSum = 0;
            for c in range(0, col):
                rowSum = rowSum + matrix[0][c];
                self.sumMatrix[0][c] = rowSum;

            colSum = 0;
            for r in range(0, row):
                colSum = colSum + matrix[r][0];
                self.sumMatrix[r][0] = colSum;

            # use dynamic programming idea
            for d1 in range(1, row):
                for d2 in range(1, col):
                    self.sumMatrix[d1][d2] = self.sumMatrix[d1-1][d2] + self.sumMatrix[d1][d2-1] - self.sumMatrix[d1-1][d2-1] + matrix[d1][d2];

        
    def sumRegion(self, row1, col1, row2, col2):

        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        if self.copyMatrix == None:
            return 0;

        if row1 == 0 and col1 == 0:
            return self.sumMatrix[row2][col2];

        elif col1 == 0 and row1 != 0:
            return self.sumMatrix[row2][col2] - self.sumMatrix[row1-1][col2];

        elif row1 == 0 and col1 != 0:
            return self.sumMatrix[row2][col2] - self.sumMatrix[row2][col1-1];

        else:
            return self.sumMatrix[row2][col2] - self.sumMatrix[row2][col1-1] - self.sumMatrix[row1-1][col2] + self.sumMatrix[row1-1][col1-1];


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
