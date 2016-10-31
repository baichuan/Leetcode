class Solution(object):

    def isHappy(self, n):

        """
        :type n: int
        :rtype: bool
        """

        sum_list = [];

        while n != 1 and n not in sum_list:

            sum_list.append(n);
            sum = 0;

            while n > 0:
                digit = int(n%10);
                sum = sum + digit * digit;
                n = int(n/10);

            n = sum;

        if n == 1:
            return True;

        else:
            return False;
