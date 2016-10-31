class Solution(object):

    def romanToInt(self, s):

        """
        :type s: str
        :rtype: int
        """

        convertDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000};
        res = 0;

        for i in range(0, len(s)):

            if i > 0 and convertDict[s[i]] > convertDict[s[i-1]]:
                res = res + (convertDict[s[i]] - 2*convertDict[s[i-1]]);

            else:
                res = res + convertDict[s[i]];

        return res;
