class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        lis = []
        while head:
            lis.append(head.val)
            head = head.next
        new = lis[::-1]
        return new