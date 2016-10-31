class Solution(object):

    def isMatch(self, s, p):

        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        # recursive solution
        
        # both p and s be empty set, then return true

        if not p:
            return not s;
            
        if p[-1] == "*":
            
	    # s = "a"
            # p = "ab*a*"

            # s = "abcdeeeee"  
            # p = "abcde*" 
            
            if s and (s[-1] == p[-2] or p[-2] == "."):
                return self.isMatch(s, p[:-2]) or self.isMatch(s[:-1], p);
                
            # s: "abcdh"  p: "abcdhe*"
            else:
                return self.isMatch(s, p[:-2]);
                
        else:
            
            if s and (s[-1] == p[-1] or p[-1] == "."):
                return self.isMatch(s[:-1], p[:-1]);
                
            else:
                return False;


class Solution(object):

    def isMatch(self, s, p):

        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        m = len(s);
        n = len(p);
        
        dp = [];

        for i in range(0, m + 1):
            
            inter_dp = [];
            
            for j in range(0, n + 1):
                inter_dp.append(False);
            
            dp.append(inter_dp);
            
        dp[0][0] = True;
        
        # if s = "", p = "c*e*" => "c*" => ""
        
        for j in range(2, n + 1):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == "*";
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if p[j - 1] == "*":
                    
                    # s: "abcdeeeee"
                    # p: "abcde*"
                    dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or (dp[i - 1][j] and (s[i - 1]  == p[j - 2] or p[j - 2] == "."));
                 
                # s = "abcde"
                # p = "abcdc"
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == ".");
                    
        return dp[-1][-1];
