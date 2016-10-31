class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        # time complexity: O(k*logn + n) and space complexity: O(n)
        r = len(matrix);
        c = len(matrix[0]);

        # put the first column of matrix into a min-heap for initialization
        # in heap, store the following information: (value, row_index, column_index)

        h = [];
        for i in range(0, r):
            heapq.heappush(h, (matrix[i][0], i, 0));

        count = 0;
        while count < k:
            triple = heapq.heappop(h);
            value = triple[0];
            row_index = triple[1];
            col_index = triple[2];
            if col_index < c - 1:
                heapq.heappush(h, (matrix[row_index][col_index+1], row_index, col_index + 1));
            count = count + 1;
        return value;
