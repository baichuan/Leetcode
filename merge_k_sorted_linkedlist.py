# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 输入: lists = [[1->2>10],[3->9],[5->6]] 输出: 1->2->3->5->6->9->10

class Solution(object):

    def mergeKLists(self, lists):

        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

	# time complexity O(k + (n-k) * lgk)

        heap = [];

        for node in lists:

            if node:
                heapq.heappush(heap, (node.val, node));
                
        # initialization

        head = ListNode(0);
        curr = head;

        while heap:

            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next

            if pop[1].next: 

                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
                
        return head.next 
