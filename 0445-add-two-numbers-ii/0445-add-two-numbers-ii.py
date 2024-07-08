# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        current = head
        l1_reversed = self.reverse_linkedlist(l1)
        l2_reversed = self.reverse_linkedlist(l2)


        while l1_reversed or l2_reversed:
            digit1 = l1_reversed.val if l1_reversed is not None else 0
            digit2 = l2_reversed.val if l2_reversed is not None else 0

            total = digit1 + digit2 + carry
            carry = total//10
            total = total % 10

            current.next = ListNode(total)
            current = current.next

            l1_reversed = l1_reversed.next if l1_reversed is not None else None
            l2_reversed = l2_reversed.next if l2_reversed is not None else None

        if carry:
            current.next = ListNode(carry)
            current = current.next
        current.next = None
        reversed_head = self.reverse_linkedlist(head.next)
        return reversed_head

    def reverse_linkedlist(self, linkedlist):
        prev = None
        current = linkedlist

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev


        