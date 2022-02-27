"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return head
        
        mappings = {}
        
        temp = head.next
        
        res = Node(head.val)
        temp2 = res
        mappings[head] = res
        
        while temp != None:
            temp2.next = Node(temp.val)
            temp2 = temp2.next
            mappings[temp] = temp2
            temp = temp.next
            
        temp, temp2 = head, res
        
        while temp != None:
            if temp.random != None:
                temp2.random = mappings[temp.random]
            temp = temp.next
            temp2 = temp2.next
            
        return res