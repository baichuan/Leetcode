class Solution(object):

    def countAndSay(self, n):

        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return '1';

        res = '1';
        for i in range(0, n-1):

            nextRes = '';
            p = 1;
            count = 1;
            currLetter = res[0];

            while p < len(res):

                if currLetter == res[p]:
                    count = count + 1;

                else:
                    nextRes = nextRes + str(count);
                    nextRes = nextRes + currLetter;
                    count = 1;
                    currLetter = res[p];

                p = p + 1;

            nextRes = nextRes + str(count);
            nextRes = nextRes + str(currLetter);

            res = nextRes;

        return res;
