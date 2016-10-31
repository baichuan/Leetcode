import os;
import sys;


# time complexity: O(n^{2})
# space complexity: O(n)

def wordBreak(s, wordDict):
 
        if not s:
            return [];
            
        dp = [[] for i in range(len(s) + 1)];
        dp[0] = [0];
        
        for i in range(0, len(s) + 1):
            for j in range(0, i):
                
                if dp[j] and s[j:i] in wordDict:
                    dp[i].append(j);
        
	print str(dp)

        # backtracking the result
	        
        res = [];
        helper(dp, s, len(s), res, "");

        return res;
        
def helper(dp, s, index, res, word):
        
        for i in dp[index]:
            temp = s[i:index] + " " + word if word else s[i:index];
            
            if i == 0:
                res.append(temp);
            
            else:
                helper(dp, s, i, res, temp);


if __name__ == "__main__":

	s = "catsanddog";
	wordDict = ["cat", "cats", "and", "sand", "dog"];

	res = wordBreak(s, wordDict);
	print str(res);
