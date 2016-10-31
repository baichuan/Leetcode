class Solution(object):

    def titleToNumber(self, s):

        """
        :type s: str
        :rtype: int
        """

        bit = len(s) - 1;
        res = 0;

        for i in range(0, len(s)):

            res = res + math.pow(26, bit) * (ord(s[i]) - ord("A") + 1);
            bit = bit - 1;

        return int(res);
