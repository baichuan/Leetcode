class Solution(object):

    def merge(self, nums1, m, nums2, n):

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

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

        for pos in range(0,m+n):
            nums1[pos] = temp_list[pos];
