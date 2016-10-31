class Solution(object):

    def generatePossibleNextMoves(self, s):

        """
        :type s: str
        :rtype: List[str]
        """

        # string doesn't support item assignment, so we have to convert string into list first
        s_list = list(s);
        res = [];

        for i in range(0, len(s_list) - 1):
            if s_list[i] == s_list[i+1] == '+':
                s_list[i] = '-';
                s_list[i+1] = '-';
                res.append(''.join(s_list));
                s_list[i] = '+';
                s_list[i+1] = '+';

        return res;
