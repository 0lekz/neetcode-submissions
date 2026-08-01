# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # how do I spit list in two if no length given?
        # slow and fast pointers!
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None

        prev = None
        # reverse the list starting node (socond hafl of entire list)
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        reverse = prev

        # merge first half and second half:
        while reverse:
            tmp1 = head.next
            tmp2 = reverse.next

            head.next = reverse
            reverse.next = tmp1
            
            # for next iter
            head = tmp1 # new head is 4
            reverse = tmp2 # new reverse is 8 
            