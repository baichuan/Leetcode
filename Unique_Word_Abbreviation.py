class ValidWordAbbr(object):

    def __init__(self, dictionary):

        """
        initialize your data structure here.
        :type dictionary: List[str]
        """

	# build a hash map: key abbreviation and value is a list of words in dictionary that matches the abbreviation

        self.dict = {};
        self.convertList = [];

        for i in range(0, len(dictionary)):
            if len(dictionary[i]) <= 2:
                self.convertList.append(dictionary[i]);

            else:
                s = dictionary[i];
                self.convertList.append(str(s[0]) + str(len(s)-2)+str(s[-1]));

        for pos in range(0, len(self.convertList)):
            if self.convertList[pos] not in self.dict:
                self.temp = [];
                self.temp.append(dictionary[pos]);
                self.dict[self.convertList[pos]] = self.temp;

            else:
                self.temp = self.dict[self.convertList[pos]];
                self.temp.append(dictionary[pos]);
                self.dict[self.convertList[pos]] = self.temp;


    def isUnique(self, word):

        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """

        if len(word) <= 2:
            if word not in self.dict.keys():
                return True;

            else:
                if len(list(set(self.dict[word])))== 1:
                    return True;
                else:
                    return False;
                    
        else:

            word_s = str(word[0]) + str(len(word)-2) + str(word[-1]);
            if word_s not in self.dict:
                return True;

            else:
                if word in self.dict[word_s] and len(list(set(self.dict[word_s]))) == 1:
                    return True;
                else:
                    return False;

        
# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
