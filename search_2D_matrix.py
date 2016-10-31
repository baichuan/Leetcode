class Solution(object):

    def searchMatrix(self, matrix, target):

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

	# time complexity: O(log (row + col))

        row_num = len(matrix);
        col_num = len(matrix[0]);

        begin = 0;
        end = row_num * col_num - 1;

       
        while begin <= end:

            mid = (begin + end) / 2;
            mid_value = matrix[mid / col_num][mid % col_num];

            if mid_value == target:
                return True;

            elif mid_value < target:
                begin = mid + 1;

            else:
                end = mid - 1;

        return False;


class Solution(object):

    def searchMatrix(self, matrix, target):

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # time complexity O(row + col)
        # start from upper rightmost position to search

        row = len(matrix);
        col = len(matrix[0]);

        i = 0;
        j = col -1;

        while i <= row-1 and j >= 0:
            if matrix[i][j] == target:
                return True;

            elif matrix[i][j] < target:
                i = i + 1;

            else:
                j = j - 1;

        return False;
