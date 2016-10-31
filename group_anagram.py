class Solution(object):

    def groupAnagrams(self, strs):

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

	# time complexity O(m*n*logn)
        dict = {}
        
        for string in strs:

            s = "".join(sorted(string));

            if s not in dict:
                dict[s] = [string];

            else:
                temp_list = dict[s];
                temp_list.append(string);
                dict[s] = temp_list;

        res_list = [];

        for x in dict:
            res_list.append(dict[x]);

        res_list.sort(key = len, reverse = True);
        
        return res_list;


# solve group anagrams without sorting

# idea: use the frequency pattern as key of hash table ["0"] * 26

class Solution(object):

    def groupAnagrams(self, strs):

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # don't use sorting
        # time complexity O(m * n)
        
        dict = {};
        
        for string in strs:
            
            arr = ["0"] * 26;
            
            for i in range(0, len(string)):
                
                arr[ord(string[i]) - ord("a")] = str(int(arr[ord(string[i]) - ord("a")]) + 1);
            
            arr_str = "".join(arr);
            
            if arr_str not in dict:

                dict[arr_str] = [string];

            else:

                dict[arr_str].append(string);
                
        res = [];
        
        for v in dict.values():
            res.append(v);
            
        return res;
