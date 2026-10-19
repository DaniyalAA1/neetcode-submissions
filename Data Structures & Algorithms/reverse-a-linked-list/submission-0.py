# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We can reverse the linked list in place by reversing the pointers between two nodes while keeping track of the next node's address. Before changing the next pointer of the current node, we must store the next node to ensure we don't lose the rest of the list during the reversal. This way, we can safely update the links between the previous and current nodes.
        # use recursion
        # base case
        # recursive call
        # im done with reversing when ive hit the end of the linkedlist and head.next is null aka None in Python
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next # store node so i dont lose next nodes pointer

            curr.next = prev # reverse pointer to point backward

            #move both these pointers one step forward in the SLL
            prev = curr
            curr = next_node
        return prev



            



        