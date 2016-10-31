# facebook follow-up: addKBinary

class Solution(object):

    def addBinary(self, a, b):

        """
        :type a: str
        :type b: str
        :rtype: str
        """

        resList = [];
        sum = 0;

        for i in range(0, max(len(a), len(b))):

            if i < len(a) and a[len(a) - 1 - i] == '1':
                sum = sum + 1;

            if i < len(b)  and b[len(b) - 1 - i] == '1':
                sum = sum + 1;

            resList.append(str(sum % 2));
            sum = sum / 2;

        if sum > 0 :
            resList.append(str(1));

        return ''.join(resList)[::-1];
