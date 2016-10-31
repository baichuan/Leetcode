class Solution(object):

    def searchMatrix(self, matrix, target):

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix);
        n = len(matrix[0]);

        i = 0;
        j = n - 1;

        while i <= m -1 and j >= 0:
            if matrix[i][j] < target:
                i = i + 1;

            elif matrix[i][j] > target:
                j = j - 1;

            else:
                return True;

        return False;
