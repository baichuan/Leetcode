class Solution(object):

    def fullJustify(self, words, maxWidth):

        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        # divide the words
        # use a funcion to adjust the spacing
        # special deal with the last line, which is fully left justified
        

        left = 0;
        right = 0;
        
        word_length = len(words);
        
        res = [];
        
        while left < word_length:
        
            L = len(words[left]);
            
            # use greedy strategy to put as many words in one line
            # the extra plus 1 is the space between two words
            
            while right + 1 < word_length and L + len(words[right + 1]) + 1 <= maxWidth:    
                
                right += 1;
                L = L + len(words[right]) + 1;
            
            # not the last line, we will write a helper function to arrange the words in one line
            if right != word_length - 1:
                res.append(self.helper(words[left:right + 1], maxWidth - L));
                
            else:
                # reach the last line
                res.append(" ".join(words[left:right + 1]) + " "  * (maxWidth - L));
                
            left = right = right + 1;
            
        return res;

        
    def helper(self, line_words, extra_length):
        
        # if the extra_length is zero, it means we don't need to add any extra empty space. Thus we join the line_words and return the result
        
        if extra_length == 0:

            return " ".join(line_words);    

        length_ = len(line_words) - 1;
        
        # if only one word, then all empty space is added to the end

        if length_ == 0:
            return line_words[0] + " " * extra_length;
            

        # otherwise we evenly distribute extra space
        extra_space = [" "] * length_;
        
        # insert extra white space in the spaces between word

        # If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right
        
        for i in range(0, extra_length):
            extra_space[i % length_] += " ";
            
        res = "";
        
        for i in range(0, length_):
            # combine word and space
            res += line_words[i] + extra_space[i]; 
        
        # add last word
        return res + line_words[-1];
