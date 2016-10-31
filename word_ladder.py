class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):

        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        # use BFS to solve question
        
        # initialize the queue as layer 0

        queue = [(beginWord, 1)];

        english_collection = 'abcdefghijklmnopqrstuvwxyz';
        
        while queue:
            
            word, dist = queue.pop(0);
            
            if word == endWord:
                return dist;

            for i in range(0, len(word)):
                
                for j in range(0, len(english_collection)):
                    
                    cand_word = word[:i] + english_collection[j] + word[i+1:];
                    
                    if cand_word in wordList:
                        
                        # build (i + 1)-th layer
                        queue.append((cand_word, dist + 1));

                        # this remove step is same as using visited_set
                        wordList.remove(cand_word);

        return 0;
