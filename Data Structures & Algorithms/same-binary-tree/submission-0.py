# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #The idea is to use a recursive call, and for definition i say that
        # two bynary tree starting ar the given root are identical iff theyr value
        # is identical and the correspoonding left child tree and right child tree are identical




        def identical(node1, node2):
            if(node1 is None and node2 is None):
                return True
            if (node1 is None and node2 is not None):
                return False
            if (node1 is not None and node2 is  None):
                return False
            else:
                result = (node1.val == node2.val) and identical(node1.right,node2.right) and    identical(node1.left,node2.left)
                return  result
                        
                




        return identical(p,q)

        