# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            start = head.next
        else:
            start = head
        pre = None
        while head:
            tmp = head.next
            if tmp:
                head.next = tmp.next
                tmp.next = head
                if pre:
                    pre.next = tmp
                pre = head
                head = head.next
            else:
                break
        return start
