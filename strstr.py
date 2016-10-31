class Solution(object):

    def strStr(self, haystack, needle):

        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        m = len(haystack);
        n = len(needle);

        if n == 0:
            return 0;

        if m < n:
            return -1;

        if needle not in haystack:
            return -1;

        else:
            return haystack.index(needle);


class Solution(object):

    def strStr(self, haystack, needle):

        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:

            return 0;
            
        if len(needle) > len(haystack):

            return -1;

        for i in range(0, len(haystack) - len(needle) + 1):
            
            if haystack[i] == needle[0]:
                
                if haystack[i:i+len(needle)] == needle:
                    
                    return i;

        return -1;
