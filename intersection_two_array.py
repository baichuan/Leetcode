class Solution(object):

    def intersection(self, nums1, nums2):

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        res_list = [];
        nums1 = set(nums1);
        for i in range(0, len(nums2)):
            if nums2[i] in nums1:
                res_list.append(nums2[i]);

        return list(set(res_list));


class Solution(object):

    def intersection(self, nums1, nums2):

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # two pointers
        # time complexity: O(m + n + m*logm + n*logn)
        
        nums1.sort();
        nums2.sort();
        
        i = 0;
        j = 0;
        
        res = set();
        
        while i < len(nums1) and j < len(nums2):
            
            if nums1[i] < nums2[j]:
                
                i += 1;
                

            elif nums1[i] > nums2[j]:
                
                j += 1;

            else:
                
                res.add(nums1[i]);
                i += 1;
                j += 1;

        return list(res);
            
