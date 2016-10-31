class Solution(object):

    def intersect(self, nums1, nums2):

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        from collections import Counter;
        res_list = [];
        dict1 = Counter(nums1);
        dict2 = Counter(nums2);
        for k1, v1 in dict1.items():
            if k1 in dict2.keys():
                v2 = dict2[k1];
                if v1 >= v2:

                    for pos in range(0, v2):
                        res_list.append(k1);

                else:
                    for pos in range(0, v1):
                        res_list.append(k1);

        return res_list;


class Solution(object):

    def intersect(self, nums1, nums2):

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # two pointers
        # time complexity: O(m + n + n*logn + m*logm)
        
        nums1.sort();
        nums2.sort();


        i = 0;
        j = 0;
        
        res = [];
        
        while i < len(nums1) and j < len(nums2):
            
            if nums1[i] < nums2[j]:
                
                i += 1;
                
            elif nums1[i] > nums2[j]:
                
                j += 1;
                
            else:
                
                res.append(nums1[i]);
                i += 1;
                j += 1;
                
        return res;
