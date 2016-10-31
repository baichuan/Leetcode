class Solution(object):

    def minWindow(self, s, t):

        """
        :type s: str
        :type t: str
        :rtype: str
        """

	# s = "DAEBGHCIJKLAMBNC"
	# t = "ABC"
        # for example, t = "ABC", so counter = {A:1, B:1, C:1}

        counter = collections.Counter(t);

        # keep the index of characters of S which in T
        window = [];
        res = "";
        
        dict = collections.defaultdict(list);
        
        for i in range(0, len(s)):
            
            if s[i] in t:
                
                dict[s[i]].append(i);
                window.append(i);
                
                if len(dict[s[i]]) > counter[s[i]]:

                    removed_index = dict[s[i]].pop(0);
                    window.remove(removed_index);
                    
                if len(window) == len(t) and (res == "" or window[-1] - window[0] + 1 < len(res)):
                    res = s[window[0]:window[-1] + 1];
                    
        return res;
