class Solution(object):

    def generate(self, numRows):

        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        # res_list[3][2] = res_list[2][1] + res_list[2][2]
        # res_list[i][j] = res_list[i-1][j-1] + res_list[i-1][j]

        if numRows == 0:
            return [];

        elif numRows == 1:
            return [[1]];

        elif numRows == 2:
            return [[1],[1,1]];

        # consider general case which numRows > 2
        elif numRows > 2:

            # initialization step
            res_list = [];
            for i in range(0, numRows):
                inner_list = [];

                for j in range(0, i + 1):
                    inner_list.append(1);
                res_list.append(inner_list);

            # update

            for pos in range(2, numRows):
                for inpos in range(1, pos):
                    res_list[pos][inpos] = res_list[pos-1][inpos-1] + res_list[pos-1][inpos];

            return res_list;
