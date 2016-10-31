# array solution

class Solution(object):

    def findTheDifference(self, s, t):

        """
        :type s: str
        :type t: str
        :rtype: str
        """

        word_count_list = [0]*26;

        for i in range(0, len(s)):
            word_count_list[ord(s[i]) - ord("a")] = word_count_list[ord(s[i]) - ord("a")] + 1;

        for j in range(0, len(t)):
            word_count_list[ord(t[j]) - ord("a")] = word_count_list[ord(t[j]) - ord("a")] - 1;

        for pos in range(0, 26):
            if word_count_list[pos]:
                return chr(pos + ord("a"));


# bit operation

class Solution(object):

    def findTheDifference(self, s, t):

        """
        :type s: str
        :type t: str
        :rtype: str
        """

        res = 0;

        for i in range(0, len(s)):
            res = res ^ ord(s[i]);

        for j in range(0, len(t)):
            res = res ^ ord(t[j]);

        return chr(res);
