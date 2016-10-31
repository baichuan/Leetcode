class Solution(object):

    def shortestDistance(self, words, word1, word2):

        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        index1 = -1;
        index2 = -1;
        min_dist = sys.maxint;

        for i in range(0, len(words)):

            if words[i] == word1:
                index1 = i;

            elif words[i] == word2:
                index2 = i;
                
            if index1 != -1 and index2 != -1:

                dist = abs(index1 - index2);
                if dist < min_dist:
                    min_dist = dist;

        return min_dist;
