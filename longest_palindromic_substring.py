class Solution(object):

    def longestPalindrome(self, s):

        """
        :type s: str
        :rtype: str
        """
        
        # palindrome is symmetric around its center
        # assume string length is n, then we have 2n - 1 centers. For example, abba
        
        # time complexity O(n^{2}), space complexity O(1)

	# example: abba
        
        start = 0;
        end = 0;
        
        for i in range(0, len(s)):
            
            length1 = self.helper(s, i, i);
            length2 = self.helper(s, i, i + 1);
            
            length = max(length1, length2);
            
            if length > end - start:
                start = i - (length - 1) / 2;
                end = i + length / 2;
                
        return s[start:end + 1];
        
        
    def helper(self, s, low, high):
        
        while low >=0 and high <= len(s) - 1 and s[low] == s[high]:
            
	    low -= 1;
            high += 1;
            
        return high - low - 1;
