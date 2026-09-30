# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # I can think about it in a recursive way.
        # Immagine that i am node i can ask the depth of each one of my leaves and return the biggest one
        # plus my contribution


        def depth(node):
            if not node:
                return 0
            
            return max(depth(node.right),depth(node.left)) + 1

        return depth(root)
        