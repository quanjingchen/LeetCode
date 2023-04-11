# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prevNode = None
        while current != None:
            nextNode = current.next
            current.next = prevNode
            prevNode = current
            current = nextNode
            
        return prevNode
        

        
        