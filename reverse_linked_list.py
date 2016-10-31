# Definition for singly-linked list.

# class ListNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseList(self, head):

        """
        :type head: ListNode
        :rtype: ListNode
        """

	#指针移动，找到next， 记录prev， 让next这个node指向prev， 然后下一轮继续这样

        dummy = ListNode(0);

        while head:

            next = head.next;
            head.next = dummy.next;
            dummy.next = head;
            head = next;
            
        return dummy.next;


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        return self.doReverse(head, None)
    def doReverse(self, head, newHead):
        if head is None:
            return newHead
        next = head.next
        head.next = newHead
        return self.doReverse(next, head)
