# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        dummy = ListNode()
        dumm = dummy
        nums = set(nums)
        resultnodes = []
        while current:
            if current.val in nums:
                value = current.val
                while current and current.val == value:
                    next = current.next
                    current = next
                
            else:
                dummy.next = current
                dummy = dummy.next
                current = current.next
        
        dummy.next = None
        return dumm.next
            
        