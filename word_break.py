class Solution(object):

    def wordBreak(self, s, wordDict):

        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """

	# time complexity O(n^{2})
	# space complexity O(n)

        if s == "":

            return True;
            

        if len(s) == 1:
            
            if s in wordDict:
                
                return True;
                
            else:
                
                return False;
                

        # initialize the bool_list for dp result
        # dp(i) represents s[0:i], left included and right excluded, can be segmented into words from dict
        # dp(i) = dp(j) + string[j:i], where j < i
        
        bool_list = [False] * (len(s) + 1);
        bool_list[0] = True;
        
        for i in range(0, len(s) + 1):
            
            for j in range(0, i):
                
                if bool_list[j] == True and s[j:i] in wordDict:
                    
                    bool_list[i] = True;
                    break;
        
        return bool_list[len(s)];
