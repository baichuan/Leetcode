class Solution(object):

    def isNumber(self, s):

        """
        :type s: str
        :rtype: bool
        """
        

        # 1. pure number +/-890092
        # 2. point number +/-1.3492 or .5 or 1.    not .
        # 3. exponent number +/-32e+/-45    not e9 nor 3e
        

        # time complexity O(n)
        # space complexity 0(1)
        
        i = 0;
        n = len(s);
        isNumeric = False;
        
        # remove the white space at the begining of the string

        while i < n and s[i] == ' ':
            i += 1;
            
        if i < n and (s[i] == "+" or s[i] == "-"):
            i += 1;
            
        while i < n and s[i].isdigit():

            isNumeric = True;
            i += 1;
            
        # handle .
        if i < n and s[i] == ".":
            i += 1;

            while i < n and s[i].isdigit():

                isNumeric = True;
                i += 1;
                

        # handle 3e10 => true

        if isNumeric and i < n and s[i] == "e":
            i += 1;
            isNumeric = False;

            if i < n and (s[i] == "+" or s[i] == "-"):
                i += 1;

                
            while i < n and s[i].isdigit():
                isNumeric = True;
                i += 1;
        
        # remove the white space at the end of string
        while i < n and s[i] == " ":
            i += 1;
        
        return isNumeric and i == n;
