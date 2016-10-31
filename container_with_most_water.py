class Solution(object):

    def maxArea(self, height):

        """
        :type height: List[int]
        :rtype: int
        """

        # two pointers
        
        l = 0;
        r = len(height) - 1;

        res = 0;

        while l < r:
            
            area = min(height[l], height[r]) * (r - l);
            res = max(res, area);

            if height[l] < height[r]:

                l = l + 1;

            else:

                r = r - 1;

        return res;
