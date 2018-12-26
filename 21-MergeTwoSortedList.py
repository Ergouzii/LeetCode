# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next # move to next node
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1: # if one of the lists ends, append the rest part of the other list
            cur.next = l1
        elif l2:
            cur.next = l2
        return dummy.next
