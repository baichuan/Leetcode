class Solution(object):

    def groupStrings(self, strings):

        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """

        convert_list = [];

        for i in range(0, len(strings)):
            temp_res = ();
            for s in strings[i]:
                temp_res = temp_res + ((ord(s) - ord(strings[i][0])) % 26,);
            convert_list.append(temp_res);

        dict = {};
        for pos in range(0, len(convert_list)):
            if convert_list[pos] not in dict:
                temp_list = [];
                temp_list.append(strings[pos]);
                dict[convert_list[pos]] = temp_list;

            else:
                temp_list = dict[convert_list[pos]];
                temp_list.append(strings[pos]);
                dict[convert_list[pos]] = temp_list;

        res = [];
        for v in dict.values():
            res.append(v);

        return res;
