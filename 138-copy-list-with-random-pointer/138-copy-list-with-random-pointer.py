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
        
        nodes_arr = []
        mappings = {}
        
        temp = head.next
        
        res = Node(head.val)
        temp2 = res
        nodes_arr.append(res)
        c = 1
        mappings[head] = 0
        
        while temp != None:
            temp2.next = Node(temp.val)
            mappings[temp] = c
            c += 1
            temp = temp.next
            temp2 = temp2.next
            nodes_arr.append(temp2)
            
            
        temp, temp2 = head, res
        
        while temp != None:
            if temp.random != None:
                temp2.random = nodes_arr[mappings[temp.random]]
            temp = temp.next
            temp2 = temp2.next
            
        return res