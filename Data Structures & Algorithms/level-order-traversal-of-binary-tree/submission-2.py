from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #basically here i need to perform a bfs with a double queue, when i have finished the
        #the first queue i append the one visited at this level and swap witht he second queue
        if not root:
            return []
        queue1 = deque()
        queue2 = deque()
        result = list()
        seen = set()

        queue1.append(root)

        current = list()
        while queue1:
            visiting = queue1.popleft()
            if visiting.left :

                queue2.append(visiting.left)
            if visiting.right :

                queue2.append(visiting.right)

            current.append(visiting.val)

            if len(queue1) ==0:
                result.append(current)
                current = list()
                if len(queue2) == 0:
                    break;
                queue1 = queue2
                queue2 = deque()
        
        

        return result