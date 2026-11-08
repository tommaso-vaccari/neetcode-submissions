# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        def rev(node, last):
            temp = node.next
            node.next = last
            if temp is None:
                return node
            
            return rev(temp, node)
        
        return rev(head, None)
        