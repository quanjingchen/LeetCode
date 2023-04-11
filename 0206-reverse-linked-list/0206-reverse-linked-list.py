# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        prevNode = None
        while pointer != None:
            nextNode = pointer.next
            pointer.next = prevNode
            prevNode = pointer
            pointer = nextNode
            
        return prevNode
        

        
        