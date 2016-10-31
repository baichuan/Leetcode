class Solution(object):

    def mySqrt(self, x):

        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0;

        if x < 0:
            return -1;

        val = x;
        last = 10000;
        eps = 0.00000001;

        while abs(val - last) > eps:
                last = val;
                val = float(val + float(x)/(val))/(2);

        return int(val);


class Solution(object):

    def mySqrt(self, x):

        """
        :type x: int
        :rtype: int
        """
        
        # binary search
        
        if x == 0 or x == 1:
            return x;
        
        low = 1;
        high = x;
        
        while low <= high:
            
            mid = (low + high) / 2;

            if int(mid * mid) == x:
                return mid;
                
            elif int(mid * mid) < x:
                
		low = mid + 1;
                ans = mid;
                
            else:
                high = mid - 1;
                
        return ans;
