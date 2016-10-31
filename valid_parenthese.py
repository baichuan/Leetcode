class Solution(object):

    def isValid(self, s):

        """
        :type s: str
        :rtype: bool
        """

        stack = [];
        stack.append(s[0]);

        for i in range(1,len(s)):

            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i]);

            else:
		# {})
                if stack == []:
                    return False;

                if s[i] == ')' and stack[-1] != '(':
                    return False;

                if s[i] == '}' and stack[-1] != '{':
                    return False;

                if s[i] == ']' and stack[-1] != '[':
                    return False;

                stack.pop();

        if stack == []:
            return True;

        else:
            return False;
