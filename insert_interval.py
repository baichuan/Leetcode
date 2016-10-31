# Definition for an interval.

# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def insert(self, intervals, newInterval):

        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        intervals.append(newInterval);
        intervals.sort(key=lambda x: x.start);
        res_list = [];
        res_list.append(intervals[0]);

        for i in range(1, len(intervals)):

            size = len(res_list) - 1;

            if intervals[i].start > res_list[size].end:
                res_list.append(intervals[i]);

            elif intervals[i].start <= res_list[size].end and intervals[i].end > res_list[size].end:
                res_list[size].end = intervals[i].end;

        return res_list;
