# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # start at head of both
        # compare values
        # put the smaller value in the new list, move to next. 
        # if one list ends just append it to the end

        # lets say our head is head.val = None and head.next = None
        # in the first step we do head.next = list1 for example
        # list1.next will have so other value. but we are iterating fur

        head = ListNode()
        res = head
        while list1 and list2:
            if list1.val<=list2.val:
                res.next = list1
                res = res.next
                list1 = list1.next
            else:
                res.next = list2
                res = res.next
                list2 = list2.next
        if list1:
            res.next = list1
        if list2:
            res.next = list2
        return head.next
        