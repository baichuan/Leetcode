class Solution(object):

    def isAnagram(self, s, t):

        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False;

        count_list = [0]*26;

        for i in range(0, len(s)):
            count_list[ord(s[i]) - ord("a")] += 1;

        for i in range(0, len(t)):
            count_list[ord(t[i]) - ord("a")] -= 1;

        for pos in range(0, len(count_list)):

            if count_list[pos] != 0:
                return False;

        return True;
