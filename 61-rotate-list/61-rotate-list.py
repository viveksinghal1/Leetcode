# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        length, temp = 1, head
        
        while temp.next != None:
            temp = temp.next
            length += 1
            
        temp.next = head
        k %= length
        c = length-k
        
        while c != 0:
            temp = temp.next
            c -= 1
            
        head = temp.next
        temp.next = None
        
        return head
        
        