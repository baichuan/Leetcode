# solution 1
class Solution(object):

    def containsNearbyAlmostDuplicate(self, nums, k, t):

        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        # using idea of sliding windows and bucket
        if k < 1 or t < 0:
            return False;

        dict = {};

        for i in range(0, len(nums)):
            key = nums[i]/(t+1);
            for j in range(key-1, key+2):
                if j in dict and abs(nums[i] - dict[j]) <= t:
                    return True;

            dict[key] = nums[i];

            if i >= k:
                val = nums[i-k];
                curr_key = val/(t+1);
                del dict[curr_key];

        return False;


# solution 2

from collections import OrderedDict

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums:
            return False
        if t < 0 or k < 1:
            return False
        window = OrderedDict()
        for idx, num in enumerate(nums):
            # bucket size should be at least 1
            key = num / max(1, t)
            for i in (key, key-1, key+1):
                if i in window and abs(window[i] - num) <= t:
                    return True
            window[key] = num
            if idx >= k:
                window.popitem(last=False)

        return False
