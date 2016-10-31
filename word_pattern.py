class Solution(object):

    def wordPattern(self, pattern, str):

        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        p_dict = {};
        s_dict = {};

        str = str.split(" ");

        if len(pattern) != len(str):
            return False;

            
        for i in range(0, len(pattern)):
            if pattern[i] not in p_dict:
                p_dict[pattern[i]] = str[i];

            else:
                p_ = p_dict[pattern[i]];
                if p_ != str[i]:
                    return False;

            if str[i] not in s_dict:
                s_dict[str[i]] = pattern[i];

            else:
                s_ = s_dict[str[i]];
                if s_ != pattern[i]:
                    return False;

        return True;
