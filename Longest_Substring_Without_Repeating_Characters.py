class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastRepeating = -1
        longestSubstring = 0
        positions = {}

        for i in range(0, len(s)):
            if s[i] in positions and lastRepeating<positions[s[i]]:
                lastRepeating = positions[s[i]]
            if i-lastRepeating > longestSubstring:
                longestSubstring = i-lastRepeating
            positions [s[i]]=i
        return longestSubstring
