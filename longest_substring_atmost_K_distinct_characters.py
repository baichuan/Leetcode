class Solution(object):

    def lengthOfLongestSubstringKDistinct(self, s, k):

        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # two pointers
        # example: "aabacbebebea" with k = 3 => "cbebebe" with length 7
        # time complexity: O(n)
        

        dict = {};
        start = 0;
        res = 0;
        
        for i in range(0, len(s)):
            
            dict[s[i]] = i;
            
            while len(dict) > k:
                
                if dict[s[start]] == start:
                    dict.pop(s[start]);
                
                start += 1;
                
            res = max(res, i - start + 1);
            
        return res;
