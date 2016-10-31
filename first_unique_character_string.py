class Solution(object):

    def firstUniqChar(self, s):

        """
        :type s: str
        :rtype: int
        """

        dict = {};

        for i in range(0, len(s)):
            if s[i] not in dict:
                count = 1;
                dict[s[i]] = count;

            else:

                count = dict[s[i]];
                count = count + 1;
                dict[s[i]] = count;

        for pos in range(0, len(s)):
            if dict[s[pos]] == 1:
                return pos;

        return -1;


class Solution(object):

    def firstUniqChar(self, s):

        """
        :type s: str
        :rtype: int
        """
        dict = {};

        for i in range(0, len(s)):
            if s[i] not in dict:
                dict[s[i]] = (1, i);

            else:
                dict[s[i]] = (dict[s[i]][0] + 1, dict[s[i]][1]);

        min_pos = sys.maxint;

        for k, v in dict.items():

            if v[0] == 1:
                curr_pos = v[1];
                if curr_pos < min_pos:
                    min_pos = curr_pos;

        if min_pos == sys.maxint:
            return -1;

        else:
            return min_pos;



class Solution(object):

    def firstUniqChar(self, s):

        """
        :type s: str
        :rtype: int
        """

        letter_list = [0]*26;

        for i in range(0, len(s)):
            letter_list[ord(s[i]) - ord("a")] = letter_list[ord(s[i])-ord("a")] + 1;

        for pos in range(0, len(s)):
            if letter_list[ord(s[pos]) - ord("a")] == 1:
                return pos;

        return -1;
