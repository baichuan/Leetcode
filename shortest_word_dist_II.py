class WordDistance(object):

    def __init__(self, words):

        """
        initialize your data structure here.
        :type words: List[str]
        """

        self.dict = {};
        for i in range(0, len(words)):

            if words[i] not in self.dict:
                index_list = [];
                index_list.append(i);
                self.dict[words[i]] = index_list;

            else:
                index_list = self.dict[words[i]];
                index_list.append(i);
                self.dict[words[i]] = index_list;

                
    def shortest(self, word1, word2):

        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """

        indexlist1 = self.dict[word1];
        indexlist2 = self.dict[word2];

        i = 0;
        j = 0;

        min_dist = sys.maxint;

        while i < len(indexlist1) and j < len(indexlist2):
            min_dist = min(min_dist, abs(indexlist1[i] - indexlist2[j]));
            if indexlist1[i] < indexlist2[j]:
                i = i + 1;

            else:
                j = j + 1;

        return min_dist;


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
