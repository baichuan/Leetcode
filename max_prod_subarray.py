class Solution(object):

    def maxProduct(self, A):

        """
        :type nums: List[int]
        :rtype: int
        """

	# keep track of [2, 3, -2, 4] => [2, 3] = 6
        result = A[0];
        min_prod = A[0];
        max_prod = A[0];

        for i in range(1,len(A)):

                temp_max_prod = max_prod;
                temp_min_prod = min_prod;

		# A[i] is either positive or negative number
                max_prod = max(max(temp_max_prod*A[i], temp_min_prod*A[i]), A[i]);
                min_prod = min(min(A[i]*temp_min_prod, A[i]*temp_max_prod), A[i]);
                result = max(result, max_prod);

        return result;
