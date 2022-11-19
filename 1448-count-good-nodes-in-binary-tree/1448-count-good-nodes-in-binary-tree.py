# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def goodNodesRec(self, root, maxvalue):
        if root == None:
            return 0
        goodNodes = 0
        if root.val >= maxvalue:
            goodNodes += 1
        maxvalue = max(root.val, maxvalue)
        goodNodes += self.goodNodesRec(root.left, maxvalue)
        goodNodes += self.goodNodesRec(root.right, maxvalue)
        return goodNodes
    
    def goodNodes(self, root: TreeNode) -> int:
        # TC -> O(N), SC -> O(H)
        goodNodesCount = self.goodNodesRec(root, root.val)
        return goodNodesCount