# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        Node = ListNode()
        dummy = Node


        while current.next:
            if current.val == 0:
                current = current.next
                nodesum = 0
                while current.val != 0:
                    nodesum += current.val
                    current = current.next
                Node.next = ListNode(nodesum, current.next)
                Node = Node.next
                

        return dummy.next
                




        