# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(head: None):
        self.head = head

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        linkedList = ListNode()
        tail = linkedList
        while list1 and list2:
            if(list1.val < list2.val):
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if(list1 is None):
            tail.next = list2
        if(list2 is None):
            tail.next = list1
        return linkedList.next

x = Solution()
x.mergeTwoLists([1,2,3], [1,2,3])
print(x)