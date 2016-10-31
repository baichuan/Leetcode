class Solution(object):

    def isPalindrome(self, s):

        """
        :type s: str
        :rtype: bool
        """

        if s.strip() == '':
            return True;

        start = 0;
        end = len(s) - 1;

        while start <= end:

            while start <= end and not s[start].isalnum():
                start = start + 1;

            while start <= end and not s[end].isalnum():
                end = end - 1;

            if start <= end and s[start].lower() != s[end].lower():
                return False;

            start = start + 1;
            end = end - 1;

        return True;


# follow-up: don't use char lower() function
class Solution(object):

    def helper(self, c1, c2):
        
        if c1.isalpha() and c2.isalpha() and ord(c1) == ord(c2):
            return True;

        if c1.isalpha() and c2.isalpha() and abs(ord(c1) - ord(c2)) == 32:
            return True;

        if c1.isdigit() and c2.isdigit() and c1 == c2:
            return True;

        return False;
        

    def isPalindrome(self, s):

        """
        :type s: str
        :rtype: bool
        """

        if s.strip() == "":
            return True;

        start = 0;
        end = len(s) - 1;

        while start <= end:
            while start <= end and not s[start].isalnum():
                start = start + 1;

            while start <= end and not s[end].isalnum():
                end = end - 1;

            if start <= end and not self.helper(s[start], s[end]):
                return False;

            start = start + 1;
            end = end - 1;

        return True;
