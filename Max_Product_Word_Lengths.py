class Solution(object):

    def maxProduct(self, words):

        """
        :type words: List[str]
        :rtype: int
        """

#	For 26 words, think it as a 26 dimensional vector. Say a word “abc”, it will represent in this vector space as “0000...000111”
# Then for two words, intersect with these 26-dimensional vectors
# In order to get 26-dimensional vector representation, use left shift operator (<<), namely 1 << (ord(s[i]) - ord(‘a’))

	# answer modified by myself based on online solution

        nums = [];
        for i in range(0, len(words)):
            sum = 0;
            set_s = list(set(words[i]));
            for j in range(0, len(set_s)):
                sum = sum +  (1 << (ord(set_s[j]) - ord('a')));

            nums.append(sum);

        ans = 0;
        for x in range(0, len(words)):
            for y in range(x+1, len(words)):
                if not (nums[x] & nums[y]):
                    ans = max(len(words[x]) * len(words[y]), ans)

        return ans;
