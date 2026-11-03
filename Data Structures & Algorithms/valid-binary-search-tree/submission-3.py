# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # a bst is valid iff all the element on the left are less than the root value and 
        # all the right element are greater than the root value and iff
        # the left subchild is a valid bst and the right subchild is a valid bst
        # So the idea is that while i descend i keep a boundary in which my element must stay

        
        def valid(node, lo, hi):
            if node is None:
                return True
            
            return lo< node.val < hi and valid(node.left, lo, node.val) and valid (node.right, node.val, hi)

        return valid(root, float("-inf"),float("inf"))

            


            


        