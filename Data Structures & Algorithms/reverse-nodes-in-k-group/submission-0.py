# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        len_list = 0
        root = head
        while root:
            len_list+=1
            root = root.next
        
        if len_list < k:
            return head
        
        swap_nums = len_list // k
        
        #print(len_list, swap_nums)
        
        root = head
        prev_tail = None
        new_head = None

        for _ in range(swap_nums):
            next_group, rev_head = self.reverse_list(root, k)

            if not new_head:          
                new_head = rev_head

            if prev_tail:             
                prev_tail.next = rev_head

            prev_tail = root          
            root = next_group         

        prev_tail.next = root         
        return new_head

    def reverse_list(self, head, k):
        temp = None
        for _ in range(k):
            nxt = head.next
            head.next = temp
            temp = head
            head = nxt
        return head, temp
