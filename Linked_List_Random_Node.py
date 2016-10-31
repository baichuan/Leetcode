# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random;
class Solution(object):

    def __init__(self, head):

        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head;


    def getRandom(self):

        """
        Returns a random node's value.
        :rtype: int
        """
        # reservior sampling (k = 1)

        r = self.head.val;
        node = self.head.next;
        cnt = 1;

        while node:
            cnt += 1
            if random.randint(1,cnt) == 1:
                r = node.val
            node = node.next

        return r

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
