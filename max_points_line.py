# Definition for a point.

# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution(object):

    def maxPoints(self, points):

        """
        :type points: List[Point]
        :rtype: int
        """

        max_points = 0;

        for i in range(0, len(points)):
            slope_list = [];
            dup_count = 0;

            for j in range(0, len(points)):

                if i != j:
                    p1 = points[i];
                    p2 = points[j];

                    if p1.x == p2.x and p1.y == p2.y:
                        dup_count = dup_count + 1;

                    elif p1.x == p2.x and p1.y != p2.y:
                        slope = 99999.00;
                        slope_list.append(slope);

                    else:
                        slope = float(p1.y - p2.y)/(p1.x - p2.x);
                        slope_list.append(slope);

            slope_count_dict = {};

            for s in range(0, len(slope_list)):
                if slope_count_dict.get(slope_list[s], -1) == -1:
                    slope_count_dict[slope_list[s]] = 1;

                else:
                    slope_count_dict[slope_list[s]] += 1;

            v_max = 0;
            for v in slope_count_dict.values():
                if v > v_max:
                    v_max = v;

            point_count = v_max + 1 + dup_count;

            if point_count > max_points:
                max_points = point_count;

        return max_points;
