# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def minMeetingRooms(self, intervals):

        """
        :type intervals: List[Interval]
        :rtype: int
        """

        if len(intervals) == 0:
            return 0;

        # sort the interval based on the starting time
        intervals.sort(key=lambda x: x.start);
        heap = [];

        # store the end time into the heap
        heapq.heappush(heap, intervals[0].end);

        for i in range(1, len(intervals)):

            if intervals[i].start >= heap[0]:
                heapq.heapreplace(heap, intervals[i].end);
            else:
                heapq.heappush(heap, intervals[i].end);

        return len(heap);
