class Solution(object):

    def productExceptSelf(self, A):

        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # idea: 1) construct a temp array left such that left[i] contains product of all elements on left of A[i] excluding A[i]
#       2) right[i]
#       3) to get prod[], multiply left[]*right[]

        length = len(A);
        left = [1] * length;
        right = [1] * lengt;
        prod = [1] * length;

        # construct left array
        for i in range(1, len(A)):
                left[i] = A[i-1] * left[i-1];

        # construct right array
        for j in range(len(A)-2, -1, -1):
                right[j] = A[j+1] * right[j+1];

        # construct product array
        for pos in range(0,len(A)):
                prod[pos] = left[pos]*right[pos];

        return prod;
