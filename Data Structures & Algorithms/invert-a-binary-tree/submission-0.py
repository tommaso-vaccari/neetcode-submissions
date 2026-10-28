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
        if not root:
            return None
        queue1 = deque()
        queue2 = deque()
        queue1.append(root)
        while queue1:
            node = queue1.popleft()
            if node:
                
                queue2.append(node.left)
                queue2.append(node.right)
            if len(queue1) == 0 and  len(queue2) >0:
                queue1 = queue2
                i = 0
                j = len(queue2) - 1

                while i < j:
                    temp = queue2[i].val
                    queue2[i].val = queue2[j].val
                    queue2[j].val = temp
                    i+=1
                    j-=1
      
                


        return root






        


        