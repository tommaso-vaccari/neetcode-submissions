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
                if node.left is not None:
                    queue2.append(node.left)
                if node.right is not None:
                    queue2.append(node.right)
            
            if len(queue1) == 0:
                queue1 = queue2
                
                if len(queue1)>0:
                    i = 0
                    j = len(queue1) - 1
                    
                    while i < j:
                        temp = queue1[i].val
                        queue1[i].val = queue1[j].val
                        queue1[j].val = temp
                        i+=1
                        j-=1
                queue2 = deque()
                
                


        return root






        


        