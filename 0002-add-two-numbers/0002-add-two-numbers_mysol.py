# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        # print(head.val)
        ans = head
        # print(ans.next)
        carry = 0
        res = []
        while l1 and l2:
            ans_value = l1.val + l2.val + carry
            carry = ans_value // 10
            ans_value = ans_value % 10
            res.append(ans_value)
            l1 = l1.next
            l2 = l2.next

        while l1:
            value = carry + l1.val
            carry = value// 10
            value  = value % 10
            res.append(value)
            l1 = l1.next
        while l2:
            value  = carry + l2.val
            carry = value//10
            value = value % 10
            res.append(value)
            l2 = l2.next
        if carry:
            res.append(carry)

        
        print(res)

        head = ListNode(res[0])
        current = head
        for num in res[1:]:
            current.next = ListNode(num)
            current = current.next 
        return head

        
