from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()

        queue.append(root)
        re = list()
        if not root:
            return []
        while queue:
            res = list()
            for _ in range(len(queue)):
                vis = queue.popleft()

                res.append(vis.val)
                if vis.left is not None:
                    queue.append(vis.left)
                if vis.right is not None:
                    queue.append(vis.right)
            re.append(res)
        return re