# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # a bst is valid iff all the element on the left are less or equal than the root value and 
        # all the right element are greater or qual than the root value and iff
        # the left subchild is a valid bst and the right subchild is a valid bst
        
        def valid(node, lo, hi):
            if node is None:         
                return True
            if not (lo < node.val < hi):   # am I inside my allowed range?
                return False
            return (valid(node.left,  lo, node.val)    # left: upper bound becomes my value
                and valid(node.right, node.val, hi))   # right: lower bound becomes my value

        return valid(root, float('-inf'), float('inf'))


            


            


        