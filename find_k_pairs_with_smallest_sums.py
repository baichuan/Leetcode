import heapq;
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        l1 = len(nums1);
        l2 = len(nums2);
        resList = [];
        if l1 * l2 <= k:
            for i in range(0, l1):
                for j in range(0, l2):
                    resList.append(([nums1[i], nums2[j]]));
            return sorted(resList, key = sum);

        minHeap = [];
        for i in range(0, l1):
            for j in range(0, l2):
                pairSum = (-1) * (nums1[i] + nums2[j]);
                if len(minHeap) < k:
                    heapq.heappush(minHeap, (pairSum, [nums1[i], nums2[j]]));
                else:
                    if minHeap[0][0] < pairSum:
                        heapq.heapreplace(minHeap, (pairSum, [nums1[i], nums2[j]]));

        for pos in range(0, len(minHeap)):
            resList.append(minHeap[pos][1]);
        return resList;
