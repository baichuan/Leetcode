class Solution(object):

    def isPowerOfFour(self, num):

        """
        :type num: int
        :rtype: bool
        """

        if num < 1:
            return False;

        while num % 4 == 0:
            num = num / 4;
        return num == 1;



# without loop solution

class Solution(object):

    def isPowerOfFour(self, num):

        """
        :type num: int
        :rtype: bool
        """

        return num>0 and num&(num-1)==0 and len("{0:b}".format(num))%2==1;
