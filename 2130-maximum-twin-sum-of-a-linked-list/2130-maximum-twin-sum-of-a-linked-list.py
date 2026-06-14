# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # Find middle of the linkedlist
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half of the linkedlist
        prev = None
        curr = slow

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        # Step 3: Find the maximum twin sum
        # 'prev' is now the head of the reversed second half
        maxSum = 0
        left = head
        right = prev

        while right:
            currSum = left.val + right.val
            maxSum = max(maxSum, currSum)

            left = left.next
            right = right.next
        
        return maxSum