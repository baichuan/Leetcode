class Solution(object):

    def topKFrequent(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
	# time complexity: O(n*logk)

        counts = collections.Counter(nums)
        heap = []
        for key, cnt in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, key))

            else:
                if heap[0][0] < cnt:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (cnt, key))

        res_list = [];
        for i in range(0, len(heap)):
            res_list.append(heap[i][1]);

        return res_list;
