"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
                return
        current=head
        dummy=Node(0)
        copy_curr=dummy
        dict1={}
        while current:
            copy_curr.next=Node(current.val)
            dict1[current]=copy_curr.next
            copy_curr=copy_curr.next
            current=current.next
        current=head
        while current:
            copy_curr=dict1[current]
            if current.random:
                copy_curr.random=dict1[current.random]
            else:
                copy_curr.random=None
            current=current.next
        return dummy.next

