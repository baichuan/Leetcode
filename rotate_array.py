class Solution(object):

    def reverse(self, A, start, end):

        while start <= end:
            A[start], A[end] = A[end], A[start];
            start = start + 1;
            end = end - 1;

    def rotate(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if len(nums) > 1:

            k = k % len(nums);
            self.reverse(nums, 0, len(nums)-1);
            self.reverse(nums, 0, k-1);
            self.reverse(nums, k, len(nums)-1);
