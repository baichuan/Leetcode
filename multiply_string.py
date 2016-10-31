class Solution(object):

    def multiply(self, num1, num2):

        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        # i ==> result's index
        # j ==> num1's index

	# example: 213 * 45 = 9585

        if num1 == '0' or num2 == '0':

            return '0';

        res = '';
        carry = 0;
        len1 = len(num1) - 1;
        len2 = len(num2) - 1;

        for i in range(0, len1 + len2 + 1):

            for j in range(0, min(i+1, len1+1)):

                if i - j <= len2:
                    carry = carry + int(num1[len1 - j]) * int(num2[len2 - (i-j)]);

            res = str(carry % 10) + res;
            carry = carry / 10;

        if carry == 0:

            return res

        else:

            return str(carry) + res;
