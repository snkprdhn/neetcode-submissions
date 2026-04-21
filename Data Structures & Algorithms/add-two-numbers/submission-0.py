# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        while l1:
            n1 *=10
            n1 += l1.val
            l1 = l1.next
        
        n2 = 0
        while l2:
            n2 *= 10
            n2 += l2.val
            l2 = l2.next
        
        n1 = int(str(n1)[::-1])
        n2 = int(str(n2)[::-1])
        n3 = n1 + n2
        print(n1, n2, n3)

        n = n3%10
        n3 = n3//10
        new_head = ListNode(n)
        l3 = new_head
        while n3:
            n = n3%10
            n3 = n3//10
            print(n)
            l3.next = ListNode(n)
            l3 = l3.next
        
        return new_head

