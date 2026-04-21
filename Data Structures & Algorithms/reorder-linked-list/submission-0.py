# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = None
        while slow:
            nex = slow.next
            slow.next = temp
            temp = slow
            slow = nex
        
        n1 = head
        n2 = temp

        # print(n1)
        # print(n2)

        while n1 and n2:
            n1_next = n1.next
            n2_next = n2.next

            n1.next = n2
            n2.next = n1_next

            n1 = n1_next
            n2 = n2_next
        

