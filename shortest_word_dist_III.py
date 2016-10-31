class Solution(object):

    def shortestWordDistance(self, words, word1, word2):

        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        index1 = -1;
        index2 = -1;
        
        if word1 != word2:

            min_dist = sys.maxint;
            for i in range(0, len(words)):
                if words[i] == word1:
                    index1 = i;
                elif words[i] == word2:
                    index2 = i;
                if index1 != -1 and index2 != -1:
                    min_dist = min(min_dist, abs(index1 - index2));

            return min_dist;

            
        elif word1 == word2:
            min_dist = sys.maxint;
            for i in range(0, len(words)):
                if words[i] == word1:
                    if index1 > index2:
                        index2 = i;

                    else: 
                        index1 = i;
                        
                    if index1 != -1 and index2 != -1:
                        min_dist = min(min_dist, abs(index1 - index2));

            return min_dist;
