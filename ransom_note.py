class Solution(object):

    def canConstruct(self, ransomNote, magazine):

        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        if ransomNote == "":
            return True;

        noteDict = {};
        for i in range(0, len(ransomNote)):
            if ransomNote[i] not in noteDict:
                noteDict[ransomNote[i]] = 1;

            else:
                noteCount = noteDict[ransomNote[i]];
                noteCount = noteCount + 1;
                noteDict[ransomNote[i]] = noteCount;

        magDict = {};
        for i in range(0, len(magazine)):
            if magazine[i] not in magDict:
                magDict[magazine[i]] = 1;
            else:
                magCount = magDict[magazine[i]];
                magCount = magCount + 1;
                magDict[magazine[i]] = magCount;

        for noteK, noteV in noteDict.items():
            if noteK not in magDict:
                return False;
            else:
                if noteK in magDict and noteV > magDict[noteK]:
                    return False;
        return True;
