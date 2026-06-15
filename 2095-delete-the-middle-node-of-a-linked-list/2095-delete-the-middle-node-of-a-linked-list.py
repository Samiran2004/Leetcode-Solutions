# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return None
        
        prevNode = head
        slowPtr = head
        fastPtr = head
        nextPtr = head

        while fastPtr is not None and fastPtr.next is not None:
            prevNode = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            nextPtr = slowPtr.next
        
        prevNode.next = nextPtr

        return head