from typing import Optional

class ListNode:
    def __init__(self, head: None):
        self.head = head
class Solution1:
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