# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(-1)
        head = dummyHead
        headList1 = list1
        headList2 = list2    
        while headList1 != None and headList2 != None:
            if headList1.val <= headList2.val:
                head.next = headList1
                headList1 = headList1.next
            else:
                head.next = headList2
                headList2 = headList2.next
            head = head.next
            
            
            
        if headList1 != None:
                head.next = headList1
            
        if headList2 != None:
                head.next = headList2
        return dummyHead.next
