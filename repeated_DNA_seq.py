class Solution(object):

    def findRepeatedDnaSequences(self, s):

        """
        :type s: str
        :rtype: List[str]
        """

        dict = {};
        for i in range(0, len(s)-9):

            sub_str = s[i:i+10];

            if dict.get(sub_str, -1) == -1:
                dict[sub_str] = 1;

            else:
                dict[sub_str] += 1;

        res_list = [];

        for k, v in dict.items():
            if v > 1:
                res_list.append(k);
        return res_list;
