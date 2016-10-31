import os;
import sys;
import collections;

class WordDictionary(object):

    def __init__(self):

        """
        initialize your data structure here.
        """

        self.dict = collections.defaultdict(list);


    def addWord(self, word):

        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """

        n = len(word);
        self.dict[n].append(word);
        

    def search(self, word):

        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        n = len(word);
        
        if n not in self.dict.keys():
            return False;
            
        for w in self.dict[n]:
            
            if self.isMatch(word, w):
                return True;
                
        return False;


    def isMatch(self, a, b):
        
        for i in range(0, len(a)):
            if a[i] != "." and a[i] != b[i]:
                return False;
                
        return True;

        
# Your WordDictionary object will be instantiated and called as such:
if __name__ == "__main__":
    
    wordDictionary = WordDictionary()
    wordDictionary.addWord("word")
    wordDictionary.addWord("pattern")
    bool_var = wordDictionary.search("pa..er.")
    print str(bool_var)


# ---------------------------------------------------------------------------------------------

# Use TrieNode for implementation

class TrieNode:

    # initialize the data structure

    def __init__(self):
        
        self.childs = dict();
        self.isWord = False;
    

class WordDictionary(object):

    def __init__(self):

        """
        initialize your data structure here.
        """

        self.root = TrieNode();
        

    def addWord(self, word):

        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """

        node = self.root;

        for letter in word:

            child = node.childs.get(letter);

            if child == None:

                child = TrieNode();
                node.childs[letter] = child;
            
            node = child;
        
        node.isWord = True;
        

    def search(self, word):

        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        return self.find(self.root, word);
        
    
    def find(self, node, word):
        
        if word == '':
            return node.isWord
            
        if word[0] == '.':
            
            for x in node.childs:

                if self.find(node.childs[x], word[1:]):
                    return True
        
        else:
            child = node.childs.get(word[0])
        
            if child:
        
                return self.find(child, word[1:])
        
        return False


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
