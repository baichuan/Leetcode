class Solution(object):

    def containsNearbyDuplicate(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        dict = {};
        for i in range(0, len(nums)):
            if dict.get(nums[i], -1) == -1:
                temp = [];
                temp.append(i);
                dict[nums[i]] = temp;

            else:
                temp = dict[nums[i]];
                temp.append(i);
                dict[nums[i]] = temp;

        for v in dict.values():
            if len(v) >= 2:
                for pos in range(0, len(v)):
                    for inpos in range(pos+1, len(v)):
                        if abs(v[pos] - v[inpos]) <= k:
                            return True;

        return False;
