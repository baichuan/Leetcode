class Solution(object):

    def isPerfectSquare(self, x):
        """
        :type num: int
        :rtype: bool
        """
        val = x;
        last = 10000;
        eps = 0.0001;
        while float(abs(val - last))/last > eps:
                last = val;
                val = float(val + float(x)/(val))/(2);

        return math.floor(val) * math.floor(val) == x;
