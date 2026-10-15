# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # beginning node has no previous node
        prev = None
        # initialize pointer to traverse linked list 
        current = head

        # iterate through linked list
        while current is not None:
            # store next node 
            next_node = current.next
            # switch link 
            current.next = prev
            # update previous variable to current node
            prev = current
            # move to next node
            current = next_node

        # return new head (not current as it points to None)
        return prev
