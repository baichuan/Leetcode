class Solution(object):

    def isIsomorphic(self, s, t):

        """
        :type s: str
        :type t: str
        :rtype: bool
        """

	# two hash tables

        s_dict = {};
        t_dict = {};

        for i in range(0, len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = t[i];

            else:
                curr_word = s_dict[s[i]];
                if curr_word != t[i]:
                    return False;

            if t[i] not in t_dict:
                t_dict[t[i]] = s[i];

            else:
                curr_word = t_dict[t[i]];
                if curr_word != s[i]:
                    return False;

        return True;
