# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #step 1: find the mid point
        if head == None or head.next == None:
            return head
        slowPointer = head
        fastPointer = head
        while fastPointer != None and fastPointer.next != None:
            prev = slowPointer
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        #step 2: split to two lists: the first half and the second half
        prev.next = None
        firstHalf = head
        secondHalf = slowPointer
        
        #step 3: reverse the second half
        prev = None
        current = secondHalf
        while current != None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        secondHalfReversed = prev
        #step 4: merge the list: firstHalf, secondHalfReversed
        dummy = ListNode(-1)
        current = dummy
        i = 0
        while firstHalf != None and secondHalfReversed != None:
            if i % 2 != 0:
                current.next = secondHalfReversed
                secondHalfReversed = secondHalfReversed.next
            else:
                current.next = firstHalf
                firstHalf = firstHalf.next
            current = current.next
            i += 1
        if firstHalf != None :
            current.next = firstHalf
        if secondHalfReversed != None:
            current.next = secondHalfReversed
            
        return dummy.next
        