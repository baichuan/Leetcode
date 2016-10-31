class Solution(object):

    def isOneEditDistance(self, s, t):

        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        length_s = len(s);
        length_t = len(t);

        if length_s == length_t:

            replace = False; 

            for i in range(0, length_s):
                
                if s[i] != t[i]:

                    if replace:
                        return False;

                    replace = True;

            return replace;

	# example: s = ACBDE, t = ABDE
        elif length_s - length_t == 1:

            for i in range(0, length_t):

                if s[i] != t[i]:
                    return s[i+1:] == t[i:];

            return True;

        elif length_t - length_s == 1:
            
            for i in range(0, length_s):

                if s[i] != t[i]:
                    return s[i:] == t[i+1:];

            return True;            

        return False;
