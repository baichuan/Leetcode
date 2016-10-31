class Solution(object):

    def canPermutePalindrome(self, s):

        """
        :type s: str
        :rtype: bool
        """

        # build a hash table: key is each word and value is frequency of the word in the string

        dict = {};
        for i in range(0, len(s)):
            if s[i] not in dict:
                dict[s[i]] = 1;

            else:
                dict[s[i]] += 1;

        evenCount = 0;
        oddCount = 0;

        for v in dict.values():

            if v % 2 == 0:
                evenCount = evenCount + 1;

            else:
                oddCount = oddCount + 1;

        if evenCount == len(dict) or oddCount == 1:
            return True;

        else:
            return False;
