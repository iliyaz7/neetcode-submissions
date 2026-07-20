# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        carry=0
        node_sum=0
        current=dummy
        val1=0
        val2=0
        while l1 or l2 or carry:
            if l1==None:
                val1=0
            else:
                 val1=l1.val
            if l2==None:
                val2=0
            else:
                val2=l2.val
            node_sum=val1+val2+carry
            carry=node_sum//10
            digit=node_sum%10
            
            current.next=ListNode(digit)
            current=current.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next



            
