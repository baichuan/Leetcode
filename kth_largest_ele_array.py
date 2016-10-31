class Solution(object):

    def findKthLargest(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heap = [];

        for pos in range(0, k):
            heapq.heappush(heap, nums[pos]);

        for pos in range(k, len(nums)):
            if nums[pos] > heap[0]:
                heapq.heapreplace(heap, nums[pos]);

        return heap[0];
