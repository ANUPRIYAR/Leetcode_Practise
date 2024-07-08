# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head 
        prev = None  # point prev to None

        while current:
            next = current.next  # already storing the next node so that it is lost after reversing
            current.next = prev  # point current.next to prev to reverse the linked 
            prev = current    # then we mark current node as prev 
            current = next    # and the next node as current

        return prev   # return prev since prev will be node pointing to the head of reversed linked list

