# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):


class Solution(object):

    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """

        currCand = 0;
        for i in range(1, n):
            if knows(currCand, i):
                # means current candidate is not celebrity
                currCand = i;

        # check whether currCand is celebrity or not
        for pos in range(0, n):
            if pos != currCand:
                if knows(pos, currCand) == False or knows(currCand, pos) == True:
                    return -1;

        return currCand;
