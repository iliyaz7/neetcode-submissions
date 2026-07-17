# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None

        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second = slow.next
        slow.next = None

        prev,curr=None,second
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        l2=prev
        l1=head
        
        while  l2:
            m1=l1.next
            m2=l2.next
            l1.next=l2
            l1=m1
            l2.next=l1
            l2=m2

        
        return None
            
        

        