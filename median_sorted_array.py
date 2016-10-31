class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m = len(nums1);
        n = len(nums2);
        temp_list = [];
        for t in range(0,m+n):
            temp_list.append(0);

           
        i = 0;
        j = 0;
        k = 0;

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp_list[k] = nums1[i];
                i = i + 1;
            else:
                temp_list[k] = nums2[j];
                j = j + 1;
            k = k + 1;

        
        # if nums1 array reaches the end 
        if i == m:
            while k < m + n:
                temp_list[k] = nums2[j];
                k = k + 1;
                j = j + 1;

        # if nums2 array reaches the end
        else:
            while k < m + n:
                temp_list[k] = nums1[i];
                k = k + 1;
                i = i + 1;

        if len(temp_list) % 2 == 0:
            index = len(temp_list) / 2;
            return float(temp_list[index] + temp_list[index-1]) / 2;
        else:
            return temp_list[len(temp_list) / 2];
