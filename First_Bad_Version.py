# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):

    def firstBadVersion(self, n):

        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            
            return 1;
            
        low = 1;
        high = n;
        
        while low < high:
            
            mid = low + (high - low) / 2; # avoid overflowing issue

            if isBadVersion(mid) == False:
                
                low = mid + 1;
                
            elif isBadVersion(mid) == True:

                high = mid;
                
        return high;
