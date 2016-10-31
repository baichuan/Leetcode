class Solution(object):

    def reverseString(self, s):

        """
        :type s: str
        :rtype: str
        """

        low = 0;
        high = len(s) - 1;
        s = list(s);

        while low < high:
            s[low], s[high] = s[high], s[low];
            low = low + 1;
            high = high - 1;

        s = "".join(s);
        return s
