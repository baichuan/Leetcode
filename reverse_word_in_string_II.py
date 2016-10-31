class Solution(object):

    def reverseHelper(self, string, start, end):

        while start < end:

            string[start], string[end] = string[end], string[start];
            start = start + 1;
            end = end - 1;

    def reverseWords(self, s):

        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """

        if s == "":
            return '';

        # first reverse the entire string
        self.reverseHelper(s, 0, len(s) - 1);

        # then reverse each word
        start = 0;
        for i in range(0, len(s)):
            if s[i].isspace():
                self.reverseHelper(s, start, i - 1);
                start = i + 1;

        # finally reverse last word
        self.reverseHelper(s, start, len(s) - 1);
