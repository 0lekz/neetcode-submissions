# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # build hashmap of visited nodes, and if we get visited twice it's a cycle?
        fast = head
        slow = head

        # use 2 pointers, one moves 1 at the time, second moves 2 at the time
        # if the cycle exists they have to meet (think of a clock)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
        