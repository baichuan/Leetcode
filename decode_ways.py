class Solution(object):

    def numDecodings(self, s):

        """
        :type s: str
        :rtype: int
        """

        # "012" => 0

        if s == "" or s[0] == "0":
            
            return 0;

        # dp[i]: number of ways to decode string from string [0: i - 1], both end included
        
        dp = [0] * (len(s) + 1);
        
        dp[0] = 1;
        dp[1] = 1;

        for i in range(2, len(s) + 1):
            
            if int(s[i - 2: i]) >= 10 and int(s[i - 2: i]) <= 26 and s[i - 1] != "0":
                
                # example: 121 => dp[0] = 1, dp[1] = 1, dp[2] = 2, dp[3] = 3;
                # 121 => ABA; LA; AU
                
                dp[i] = dp[i - 2] + dp[i - 1];
                
            elif int(s[i - 2: i]) == 10 or int(s[i - 2: i]) == 20:
                
                # example: 120 => dp[0] = 1, dp[1] = 1, dp[2] = 2, dp[3] = dp[1] = 1
                # 120 => AT

                dp[i] = dp[i - 2];
                
            elif s[i - 1] != "0":
                
                # example: 135 => dp[0] = 1, dp[1] = 1, dp[2] = 2, dp[3] = dp[2] = 2
                # 135 => ACE, ME
                
                # example: 109 => dp[0] = 1, dp[1] = 1, dp[2] = 1, dp[3] = 1
                # 109 => JI
                
                dp[i] = dp[i - 1];
                
            else:
                
                # example: 130 => 0
                
                return 0;
                
        return dp[len(s)];
