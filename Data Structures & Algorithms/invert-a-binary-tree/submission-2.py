from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # This is classical problem in which i need to apply the bfs algorith.
        # I need to traverse the tree by levels. Then i can reconstruct it backward by flipping the arrays 
        # in which i stored the content
       
        def invertChild(node):
            if not node:
                return None
            
            node.left, node.right = invertChild(node.right), invertChild(node.left)
            return node
        
        return invertChild(root)




        


        