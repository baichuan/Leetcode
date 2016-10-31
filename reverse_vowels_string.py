class Solution(object):
    def reverseVowels(self, s):

        """
        :type s: str
        :rtype: str
        """

        if s == "":
            return "";

        vowels = ["a", "e", "i", "o", "u"];

        length = len(s) - 1;
        left = 0;
        right = length;
        s_list = list(s);

        while True:

            while left < length and s_list[left].lower() not in vowels:
                left = left + 1;

            while right >= 0 and s_list[right].lower() not in vowels:
                right = right - 1;

            # change the position of s[left] and s[right]

            if left > right:
                break;

            s_list[left], s_list[right] = s_list[right], s_list[left];
            left = left + 1;
            right = right - 1;
                
        return "".join(s_list);
